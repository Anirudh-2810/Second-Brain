---
module: "ai-ml"
topic: "Proximal Policy Optimization (PPO) — loss derivation & code"
tags: [ai, rl, policy-gradient, ppo, gae, actor-critic, derivation]
last_updated: "2026-08-09"
---

# Proximal Policy Optimization (PPO)

> **Sources:** [[raw-sources/btech roadmap]] (Track B — RL: policy gradient → PPO assignment), plus standard RL literature (Schulman et al., 2017).

A complete derivation of the PPO objective starting from the reinforcement-learning fundamentals — with GAE advantage estimation, clipped objective, and runnable code.

---

## 1. The RL setting (MDP)

- **State** $s \in \mathcal S$, **action** $a \in \mathcal A$, **reward** $r(s, a)$.
- **Policy** $\pi_\theta(a|s)$ (a distribution over actions, parameterized by $\theta$).
- **Trajectory / episode:** $\tau = (s_0, a_0, r_0, s_1, \dots)$.
- **Return (discounted):** $G_t = \sum_{k\ge0} \gamma^k r_{t+k}$.
- **Objective (maximize expected discounted return):**

$$
J(\theta) = \mathbb E_{\tau\sim\pi_\theta}\big[G_0\big]
= \mathbb E_\tau\Big[ \sum_t r_t \Big].
$$

---

## 2. Policy-gradient theorem

**Review (REINFORCE / policy gradient):** the score-function trick rewrites the gradient of $J$ without differentiating through the environment:

$$
\nabla_\theta J = \mathbb E_{s_t,a_t\sim\pi_\theta}\Big[ \nabla_\theta \log \pi_\theta(a_t|s_t) \; A_t \Big]
$$

where $A_t$ is the **advantage** (how much better than baseline).

**Intuition / mini-derivation.** Using $\nabla_\theta \pi_\theta = \pi_\theta \nabla_\theta \log\pi_\theta$,

$$
\nabla_\theta J = \sum_s \mathbb E_\tau\!\Big[ \sum_{t} R_t \frac{\pi_\theta(a_t|s_t)}{\pi_\theta(a_t|s_t)} \nabla_\theta \log\pi_\theta(a_t|s_t)\Big]
$$

(reweight by importance sampling between the sampled policy and the target at each step). Subtracting a state-dependent *baseline* $b(s_t)$ (any function that doesn't depend on $a_t$, e.g. $V(s_t)$) removes variance without changing the mean:

$$
A_t = R_t - b(s_t), \qquad \mathbb E_{a_t}[ \nabla_\theta\log\pi\, b(s_t) ] = b(s_t) \nabla_\theta \sum_a \pi(a|s) = 0.
$$

Using the return minus value function, $A_t = Q(s_t,a_t) - V(s_t)$.

### Why is this unstable?

The updates can change $\pi$ hugely in one step, destroying the estimate grounded in old data — leading to oscillations. **PPO's contribution:** take the largest step that *improves* the clipped objective, constraining the new policy to stay near the old.

---

## 3. Advantage estimation: GAE(λ)

Rather than one-step TD or plain Monte Carlo returns, **Generalized Advantage Estimation** (Schulman et al., 2016) blends them to control bias-variance:

Define the discount factor $\gamma$ and the TD-1 error:

$$
\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t).
$$

Then

$$
A_t^{(\lambda)} = \sum_{\ell \ge 0} (\gamma\lambda)^{\ell}\, \delta_{t+\ell}.
$$

- $\lambda=0$ → TD-1 (high bias, low variance).
- $\lambda=1$ → pure return MC (low bias, high variance).
- $\lambda \in (0,1)$ trades off. Empirically $\lambda \approx 0.95$, $\gamma \approx 0.99$ work well on continuous tasks.

---

## 4. PPO objective (the core derivation)

### 4.1 Trust-region problem (TRPO)

Starting from the surrogate objective of TRPO (Kakade–Langford / TRPO):

$$
L^{\mathrm{CPI}}(\theta) = \mathbb E_{t}\Big[ \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_\mathrm{old}}(a_t|s_t)} A_t \Big]
$$

where CPI = conservative policy iteration. Without a constraint, maximizing $L^{CPI}$ can jump too far. TRPO adds a hard KL constraint:

$$
\max_\theta \; \mathbb E_t\!\Big[ r_t(\theta) A_t\Big]
\qquad \text{s.t.} \quad \mathbb E_t\big[ \mathrm{KL}[\,\pi_{\theta_\mathrm{old}}, \pi_\theta\,]\big] \le \delta.
$$

TRPO solves it with a second-order approximation — **expensive** (Hessian-vector products, line search).

### 4.2 The clipped surrogate — PPO

PPO replaces the constraint with a **penalty applied by clipping the importance ratio**:

Let the probability ratio be

$$
r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_\mathrm{old}}(a_t|s_t)}.
$$

Then the **clipped PPO objective** is

$$
\boxed{\;
L^{\mathrm{CLIP}}(\theta) = \mathbb E_t\bigg[ \min\Big( r_t(\theta)\, A_t,\; \operatorname{clip}(r_t(\theta),\, 1-\varepsilon,\, 1+\varepsilon)\, A_t \Big) \bigg]
\;}
$$

with typically $\varepsilon = 0.2$.

### 4.3 Why the clip works (step-by-step reasoning)

1. If $A_t > 0$ (this action was better than baseline): $r_t$ wants $\to$ large (increase $\pi_\theta$ of that action). The clip caps ratio at $1+\varepsilon$: **no incentive to push the probability of a good action arbitrarily high in one step.**
2. If $A_t < 0$ (worse than baseline): $r_t$ wants $\to$ small. The min forces at most the *uncapped* term; but the clip term cuts the magnitude of the negative slope at $r<1-\varepsilon$ — limiting how far the policy shifts to avoid that action in one step.
3. The overall effect: the surrogate is a **lower bound** on the true reward signal, reliably **pessimistic**, and its gradient is zero outside the trusted region $[1-\varepsilon,\,1+\varepsilon]$ — a *linearized* trust-region method that needs only first-order optimization (Adam).

**The min + clip combination** gives the *conservative* (worst-case) of the two branches — never letting the objective overestimate improvement beyond the trust region.

### 4.4 The complete multi-term loss

The full PPO loss also includes a **value-function** term and an **entropy** bonus:

$$
L_t^{\mathrm{full}}(\theta) = \hat{\mathbb E}_t\Big[ L^{\mathrm{CLIP}}(\theta)
  - c_1\, \underbrace{\big(V_\theta(s_t) - V_t^{\mathrm{target}}\big)^2}_{\text{value loss MSE}}
  + c_2\, \underbrace{S[\pi_\theta](s_t)}_{\text{entropy bonus}}\Big]
$$

- **Value loss:** regression toward the bootstrapped target $V_t^{\mathrm{target}} = r_t + \gamma V_{\theta_\mathrm{old}}(s_{t+1})$ (or returns with GAE).
- **Entropy bonus** encourages exploration early on; $c_2$ decayed over training.
- **Shared backbone** (single actor-critic network) is the common architecture.

---

## 5. What actually happens per step (training loop)

```
repeat:
   1. run N actors (or a single env) for T steps using current policy π_old
   2. collect (s, a, r, s', done)
   3. compute GAE advantages A_t with target V
   4. for K epochs, minibatch SGD:
        maximize clipped surrogate L^CLIP
        (plus value loss + entropy)  → update θ
   5. θ_old ← θ
```

An important practical note: **clip fraction** (share of samples hitting the cap) is used diagnostically — if tiny, ε can be lowered.

---

## 6. Architecture diagram — PPO agent

```
          ┌──────────────────────────────────────┐
          │          ENVIRONMENT(s)              │
          │   order book / gym / trading sim     │
          └──────────────┬───────────────────────┘
                         │ s, r
          ┌──────────────▼───────────────────────┐
          │        ACTOR-CRITIC NN (θ)           │
          │   π_θ(a|s)      V_θ(s)               │
          └──────┬──────────────┬────────────────┘
                 │ π(a|s)       │ V(s)
                 ▼              ▼
          ┌──────────────┐  ┌──────────────┐
          │   rollout    │  │  GAE compute │
          │    buffer    │  │   A_t(λ)     │
          └──────┬───────┘  └──────┬───────┘
                 └────────┬────────┘
                          ▼
          ┌───────────────────────────────┐
          │  CLIPPED surrogate + value     │
          │  + entropy → Adam update θ     │
          └───────────────────────────────┘
```

---

## 7. Code Gallery

### 7.1 Python + PyTorch

```python
"""Vectorized PPO actor-critic (single-env streaming) with GAE + clipping."""
from __future__ import annotations
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim


class ActorCritic(nn.Module):
    def __init__(self, obs_dim: int, act_dim: int):
        super().__init__()
        self.shared = nn.Sequential(nn.Linear(obs_dim, 64), nn.Tanh(),
                                    nn.Linear(64, 64), nn.Tanh())
        self.policy = nn.Linear(64, act_dim)          # logits (discrete)
        self.value = nn.Linear(64, 1)

    def action_dist(self, obs: torch.Tensor):
        x = self.shared(obs)
        logits = self.policy(x)
        return torch.distributions.Categorical(logits=logits), self.value(x)


def collect_rollout(env, model, steps: int, gamma: float, lam: float):
    """Interactive env (reset/step protocol) -> (obs,a,logp,adv,ret) arrays."""
    obs = torch.tensor(env.reset(), dtype=torch.float32)
    obs_l, act_l, logp_l, rew_l, done_l = [], [], [], [], []
    with torch.no_grad():
        for _ in range(steps):
            dist, v = model.action_dist(obs)
            a = dist.sample()
            next_s, r, done, _ = env.step(a.item())
            obs_l.append(obs); act_l.append(a); logp_l.append(dist.log_prob(a))
            rew_l.append(r); done_l.append([[done]])
            obs = torch.tensor(next_s, dtype=torch.float32) if not done else torch.tensor(env.reset(), dtype=torch.float32)
    obs_l = torch.stack(obs_l); act_l = torch.stack(act_l)
    logp_l = torch.stack(logp_l).squeeze(-1)
    rew_a = np.array(rew_l, dtype=np.float32); done_a = np.array(done_l, dtype=np.float32)

    # GAE computation (backward through trajectory)
    with torch.no_grad():
        _, vs = model.action_dist(obs_l)
        vs = vs.squeeze(-1)
        # append bootstrap value: V of final state (0 for done)
        vnext = torch.zeros(1) if done_a[-1, 0] else vs[-1:]
        allv = torch.cat([vs, vnext])                    # (steps+1,)
        adv = torch.zeros(steps)
        gae = 0.0
        for t in reversed(range(steps)):
            delta = rew_a[t] + gamma * (1 - done_a[t, 0]) * allv[t+1] - allv[t]
            gae = delta + gamma * lam * (1 - done_a[t, 0]) * gae
            adv[t] = gae
        ret = adv + vs
    return obs_l, act_l, logp_l, adv, ret


def train_ppo(model, opt, data, epochs=4, clip_eps=0.2, c1=0.5, c2=0.01):
    obs, act, old_logp, adv, ret = data
    adv = (adv - adv.mean()) / (adv.std() + 1e-8)        # normalize advantages
    for _ in range(epochs):
        dist, v = model.action_dist(obs)
        logp = dist.log_prob(act)
        ratio = torch.exp(logp - old_logp)
        surr1 = ratio * adv
        surr2 = torch.clamp(ratio, 1-clip_eps, 1+clip_eps) * adv
        policy_loss = -torch.min(surr1, surr2).mean()
        value_loss = ((v.squeeze(-1) - ret) ** 2).mean()
        entropy = dist.entropy().mean()
        total = policy_loss + c1 * value_loss - c2 * entropy
        opt.zero_grad(); total.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 0.5)  # stabilize
        opt.step()
    return float(policy_loss), float(value_loss)


if __name__ == "__main__":
    # CartPole stand-in harness
    import gymnasium as gym
    env = gym.make("CartPole-v1")
    model = ActorCritic(4, 2)
    opt = optim.Adam(model.parameters(), lr=3e-4)
    for it in range(1000):
        data = collect_rollout(env, model, steps=256, gamma=0.99, lam=0.95)
        pl, vl = train_ppo(model, opt, data)
        if it % 100 == 0:
            print(f"iter {it}: policy_loss={pl:.4f} value_loss={vl:.4f}")
```

### 7.2 C++20 sketch — GAE + clipped update math (torch-free, illustrative)

```cpp
// ppo_core.hpp  (C++20): core stats used inside a gradient loop.
#pragma once
#include <vector>
#include <concepts>
#include <cmath>

namespace qf {

template <std::floating_point T>
std::vector<T> gae(const std::vector<T>& r, const std::vector<T>& v,
                   T gamma, T lam, T v_last, bool done_last) {
    const auto n = r.size();
    std::vector<T> adv(n), delta(n);
    T running = 0;
    for (int t = (int)n - 1; t >= 0; --t) {
        const T vnext = (t == (int)n - 1) ? (done_last ? T{0} : v_last) : v[t + 1];
        delta[t] = r[t] + gamma * vnext - v[t];
        running = delta[t] + gamma * lam * running;
        adv[t] = running;
    }
    return adv;
}

// importance ratio: pi_theta(a|s) / pi_old(a|s)  (passed in precomputed)
template <std::floating_point T>
T clipped_surrogate(T ratio, T advantage, T eps) {
    const T lo = ratio < (1 - eps) ? ratio : (1 - eps);
    const T hi = ratio > (1 + eps) ? ratio : (1 + eps);
    const T unclipped = ratio * advantage, clipped = hi * advantage;
    return advantage > 0 ? std::min(unclipped, clipped) : std::max(ratio*advantage, (ratio<lo?0:0));
}
} // namespace qf
```

---

## 8. PPO in finance: typical usecases

- **Optimal execution / market making** (action = order type & size; reward = slippage-adjusted P&L) — links to [[market-microstructure]].
- **Portfolio rebalancing** RL agents (state = returns/weights; reward = risk-adjusted return).
- **Alternative-data signal exploitation** with a learned policy over a traditional strat.

Always **wrap the environment in the sim** ([[event-driven-backtesting]]) and validate OOS — RL lets you overfit faster than you can spam samples (see [[model-selection-and-model-risk]]).

---

## 9. Related

- [[transformers-attention-detail]] — representation backbone for state encoding
- [[quant-toolkit-and-skills]] · [[event-driven-backtesting]] · [[market-microstructure]]