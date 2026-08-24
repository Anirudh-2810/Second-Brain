---
course_code: "DATA-SCI"
course_name: "Data Science & Machine Learning Field"
unit: "Repo 13 — terryum/awesome-deep-learning-papers (The Canon)"
tags: [deep-learning, papers, reading-list, history, linked-repo]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/terryum/awesome-deep-learning-papers"
---

## For future agent
The most-cited DL papers list (250–500 citation threshold), expanded from its real section headings (fetched 2026-08-24). This page converts the paper dump into a *reading order* with what each cluster contributed. Paper-reading method + vault integration included.

# Awesome Deep Learning Papers — Expanded

## Its Section Structure (= the field's genealogy)

1. **Understanding / Generalization / Transfer**
2. **Optimization / Training Techniques**
3. **Unsupervised / Generative Models**
4. **Convolutional Neural Network Models**
5. **Image: Segmentation / Object Detection**
6. **Image / Video / Etc**
7. **Natural Language Processing / RNNs**
8. **Speech / Other Domain**
9. **Reinforcement Learning / Robotics**
10. Plus: More-from-2016, New papers, Old papers, HW/SW/Datasets, Books/Surveys, Video lectures/blogs, "More than Top-100" appendix

## Suggested Reading Order (genealogical, 12-paper spine)

| # | Paper | Why It Changed Things |
|---|-------|----------------------|
| 1 | Krizhevsky et al., **AlexNet** (2012) | ImageNet moment; GPUs+ReLU+dropout win big |
| 2 | Simonyan & Zisserman, **VGG** | Depth via uniform small kernels; simplicity as design |
| 3 | He et al., **ResNet** | Skip connections made 100+ layers trainable |
| 4 | Szegedy et al., **GoogLeNet/Inception** | Multi-scale features in parallel |
| 5 | Hinton et al., **Dropout** | The regularization everyone uses |
| 6 | Ioffe & Szegedy, **Batch Normalization** | Training stability/speed unlock |
| 7 | Kingma & Ba, **Adam** | Default optimizer lineage |
| 8 | Goodfellow et al., **GANs** | Generative modeling via adversarial game |
| 9 | Mikolov et al., **word2vec** | Embeddings as representation idea |
| 10 | Sutskever et al., **Seq2Seq** | Encoder-decoder framing |
| 11 | Vaswani et al., **Attention Is All You Need** | Transformers — everything since |
| 12 | Mnih et al., **DQN** | RL + deep nets at human-level play |

## How to Read a Paper (protocol)

```mermaid
flowchart TD
    P1["Pass 1 (10 min):<br/>title/abstract/figures/conclusion"] --> P2{"Worth pass 2?"}
    P2 -->|"yes"| P3["Pass 2 (30 min):<br/>skim method + results,<br/>ignore proofs"]
    P2 -->|"no"| X["Log one line in vault:<br/>what it's famous for"]
    P3 --> P4["Pass 3 (only for your niche):<br/>re-derive key equation,<br/>note limitations"]
    P4 --> V["Vault note: summary +<br/>why it mattered + 1 critique"]
```

## Failure Points

| Failure | Counter |
|---------|---------|
| Reading cover-to-cover chronologically | Spine-of-12 above first; cluster reads later by need |
| Drowning in math on pass 1 | Passes are designed to defer math; trust the process |
| Reading without era context | For each: ask "what couldn't people do BEFORE this?" |

## Example Checkpoint Questions

1. What specific problem did ResNet's skip connections solve?
2. Why did batch norm allow larger learning rates?
3. Name one thing attention replaced, and why that replacement scaled better.

## Deep Edition Addendum

**Failure modes of paper-list users**:

| Failure | Mechanism | Counter |
|---------|-----------|---------|
| Chronological grind | Reading 100 papers in citation order | Spine-of-12 first; clusters by need later |
| Math wall on pass 1 | Proofs attempted too early | Passes are designed to DEFER math; trust protocol |
| Collection without extraction | Papers "read", nothing retained | Vault note per paper: claim + why-mattered + 1 critique |
| Era confusion | 2012 techniques judged by 2026 standards | Ask per paper: "what couldn't people do BEFORE this?" |

**Premortem**: *"Read deep learning papers" phase lasted 3 weeks.* Findings: started with ResNet paper's appendices; no notes; no connection to any running experiment. Paper reading works only anchored to a current build ("I'm using attention — now read the paper").

**Rescue flowchart**:
```mermaid
flowchart TD
    S["Paper reading stalled"] --> Q{"Which stuck?"}
    Q -->|"can't finish pass 1"| T["10-min rule: abstract +<br/>figures + conclusion ONLY.<br/>Log one line, move on"]
    Q -->|"math opaque"| M["Defer to pass 3;<br/>find a blog explainer first"]
    Q -->|"no anchor"| A["Anchor: read ONLY papers behind<br/>tools your current project uses"]
    T & M & A --> N["One-line vault log<br/>per paper - streak visible"]
```

**Life integration**: one spine-paper/week during DL stage; extraction line into vault daily-notes; metrics = spine completed, papers-with-notes ratio (target 100%), re-reads of own notes.

## Cross-Vault Links

- [[ml-theory-and-moocs]] · [[curated-reading-list]] (Distill essays = modern readable versions of several ideas)
- [[modules/ai/sub-notes/MODULE_5_PLANNING_NEURAL_NETWORKS]] — coursework-side NN basics