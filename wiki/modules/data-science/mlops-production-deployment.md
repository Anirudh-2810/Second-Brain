---
course_code: "DATA-SCI"
course_name: "Data Science & Machine Learning Field"
unit: "Module 5 — MLOps, Production & Model Interpretation"
tags: [mlops, deployment, production-ml, ray, distributed-computing, tensorflow-lite, model-interpretation, gradio]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#data-science-deployment--production"
---

## For future agent
Production-side ML from the knowledge repo. The repo itself was thin here (one entry: Ray), so this page also consolidates the TF production stack and model interpretation/visualization tools scattered across the source's framework sections. Use when a trained model needs to serve traffic, run distributed training, or be explained to humans.

# MLOps & Production ML

## Distributed Computing
- **[Ray](https://github.com/ray-project/ray)** — fast framework for distributed Python apps; bundles:
  - **RLlib** — scalable reinforcement learning library
  - **Tune** — scalable hyperparameter tuning
  - As of 2026: Ray is the standard for distributed Python ML workloads (high confidence)

## TensorFlow Production Stack

| Tool | Purpose | Link |
|------|---------|------|
| **TFRT** | Performant modular TF runtime (next-gen execution) | [github.com/tensorflow/runtime](https://github.com/tensorflow/runtime) |
| **TensorFlow Lite** | Mobile/embedded inference | [tensorflow.org/lite](https://www.tensorflow.org/lite/) |
| **TensorFlow.js** | Browser inference/training | [DL in browser guide](https://towardsdatascience.com/deep-learning-in-your-browser-a-brisk-guide-ca06c2198846) |
| CPU inference tuning | Intel MKL optimizations for serving | [Intel guide](https://software.intel.com/content/www/us/en/develop/articles/maximize-tensorflow-performance-on-cpu-considerations-and-recommendations-for-inference.html) |

Deployment path pattern: train (TF/Keras) → convert (TFLite for mobile / TFJS for browser / SavedModel+TFRT for servers).

## Model Interpretation & Visualization

| Tool | What It Does | Link |
|------|-------------|------|
| **tf-explain** | Interpretability callbacks (Grad-CAM etc.) during Keras training | [guide](https://gilberttanner.com/blog/interpreting-tensorflow-model-with-tf-explain) |
| **Gradio** | Quick web UI around any model — demo models interactively | [github.com/gradio-app/gradio](https://github.com/gradio-app/gradio) |
| **TensorSpace** | 3D neural-network visualization built on TensorFlow.js | [github.com/tensorspace-team/tensorspace](https://github.com/tensorspace-team/tensorspace) |

## Related Reading (from [[curated-reading-list]])

- Airbnb's knowledge platform ("Scaling Knowledge at Airbnb") — org-level ML knowledge sharing
- Pachyderm — reproducible data science pipelines
- Docker-for-data-science walkthroughs (Jupyter containers)
- "Ask HN: production ML pipeline" thread — practitioner snapshots

## Cross-Vault Links

- Full deployment context (non-ML): [[software-dev-general]] → CI/CD section; [[systems-design-distributed]] → Docker/K8s best practices
- Course bridging theory→production: [Full Stack Deep Learning](https://course.fullstackdeeplearning.com/) in [[ml-theory-and-moocs]]
- [[modules/data-science/index|Data Science Hub]] — module hub