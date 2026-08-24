---
course_code: "DATA-SCI"
course_name: "Data Science & Machine Learning Field"
unit: "Module 4 — Python for Data Science: Topics"
tags: [data-science, computer-vision, action-recognition, face-recognition, object-detection, nlp, time-series, recommender-systems, reinforcement-learning, anomaly-detection]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#python-for-data-science-by-topic"
---

## For future agent
Problem-type organized resources: given a task (detect faces, forecast a series, build a recommender), find the technique + reference repos here. The computer-vision section is deep (action recognition especially — 15+ repos). Links are research-repo era (2017-2020); architectures still teach well even where newer SOTA exists.

# Python for Data Science — By Topic

## Anomaly Detection
- [Anomaly Detection, Recommender Systems & Scaling overview](https://towardsdatascience.com/machine-learning-basics-part-4-anomaly-detection-recommender-systems-and-scaling-b8bbf0413aa9)
- [Online anomaly detection (stats.SE)](https://stats.stackexchange.com/questions/343579/online-anomaly-detection) — streaming setting
- [CV for anomaly detection with autoencoders](https://datascience.stackexchange.com/questions/37396/cross-validation-for-anomaly-detection-using-autoencoder)
- [Model Selection for Anomaly Detection (arXiv 1707.03909)](https://arxiv.org/abs/1707.03909)
- [ML class notes L16: Anomaly Detection](https://machine-learning-class-notes.readthedocs.io/en/latest/lecture16.html)

## Computer Vision

### Action Recognition & Detection (largest subsection)
**Curated list**: [awesome-action-recognition](https://github.com/jinwchoi/awesome-action-recognition)

| Repo | Approach |
|------|----------|
| [ACAM demo](https://github.com/oulutan/ACAM_Demo) | Actor Conditioned Attention Maps, real-time |
| [twostream-attention](https://github.com/pedro-abreu/twostream-attention) | 2-stream CNN + attention filtering |
| [realtime-action-detection](https://github.com/gurkirt/realtime-action-detection) | Real-time detection |
| [action-detection (SSN)](https://github.com/yjxiong/action-detection) | Temporal action detection with SSN |
| [UntrimmedNet](https://github.com/wanglimin/UntrimmedNet) | Weakly supervised recognition+detection |
| [Human-Action-Recognition-with-Keras](https://github.com/oswaldoludwig/Human-Action-Recognition-with-Keras) | Accessible Keras impl |
| [CBR](https://github.com/jiyanggao/CBR) | Cascaded boundary regression |
| [tensorflow_video_rnn (dRNN)](https://github.com/zkl99999/tensorflow_video_rnn) | Deep RNN action detection |
| [ss-tad](https://github.com/shyamal-b/ss-tad) | Single-stream temporal detection in untrimmed video |
| [JAANet](https://github.com/ZhiwenShao/JAANet) | Joint facial AU detection + alignment w/ attention |
| [HCN-pytorch](https://github.com/huguyuehuhu/HCN-pytorch) | Skeleton co-occurrence features |
| [Cross-Dataset-Action-Detection](https://github.com/aelnouby/Cross-Dataset-Action-Detection) | Cross-dataset crowded scenes |
| [graph_distillation (Google)](https://github.com/google/graph_distillation) | Graph distillation for detection |
| [KinectOnlineActionDetection](https://github.com/AmrSaleh/KinectOnlineActionDetection) | Real-time Kinect-based |

### Face Recognition & Facial Analysis
- **[face_recognition (ageitgey)](https://github.com/ageitgey/face_recognition)** — "world's simplest" facial recognition API; the standard starter
- [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace) — facial action units, open-source
- [DeepFaceLab](https://github.com/iperov/DeepFaceLab) / [faceswap](https://github.com/deepfakes/faceswap) — face replacement tooling
- [DRML (deep region multi-label)](https://github.com/zkl20061823/DRML) · [AUNets (multi-view AU detection)](https://github.com/BCV-Uniandes/AUNets) · [DRML_pytorch](https://github.com/AlexHex7/DRML_pytorch)
- ROS bridge: [ros_people_object_detection_tensorflow](https://github.com/cagbal/ros_people_object_detection_tensorflow)

### Object Detection & Segmentation
- **[Detectron2 (Meta/Facebook)](https://github.com/facebookresearch/detectron2)** — PyTorch detection framework, industry standard
- [video-object-removal](https://github.com/zllrunning/video-object-removal) — bounding box → object removal

### Other CV
- [Optical flow explained + DL relevance](https://medium.com/swlh/what-is-optical-flow-and-why-does-it-matter-in-deep-learning-b3278bb205b5)
- [Multi-label classification with SmallerVGGNet+Keras (pyimagesearch)](https://www.pyimagesearch.com/2018/05/07/multi-label-classification-with-keras)
- OCR: [Tesseract + OpenCV deep-learning text recognition (learnopencv)](https://www.learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/)
- Framework: [Videoflow](https://github.com/videoflow/videoflow) — multiprocessing video-analysis pipeline framework

## NLP
- **[HuggingFace Transformers](https://github.com/huggingface/transformers)** — SOTA models for TF2.0/PyTorch; now the de-facto NLP library (2026 note)
- [ULMFiT — universal language model classification (fast.ai)](http://nlp.fast.ai/classification/2018/05/15/introducting-ulmfit.html)
- [Topic modeling with Gensim](https://www.udemy.com/understand-javascript/) *(source link mismatched in original repo)*
- Text summarization eval: [sumeval](https://github.com/chakki-works/sumeval)

## Speech Recognition
- [Speech Recognition in Python (realpython)](https://realpython.com/python-speech-recognition/)

## Time Series
- **[Open ML Course Topic 9: Time Series in Python](https://medium.com/open-machine-learning-course/open-machine-learning-course-topic-9-time-series-analysis-in-python-a270cb05e0b3)** — best single intro (trends, seasonality, ARIMA-family)
- [ARIMA forecasting guide in Python 3](https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3)
- SARIMAX convergence pitfalls: [MLE convergence errors with statespace SARIMAX](https://stats.stackexchange.com/questions/313426/mle-convergence-errors-with-statespace-sarimax)
- Vault link: [[modules/quant-finance/forecasting-and-market-efficiency]] — financial time series context

## Recommender Systems
- **[Microsoft Recommenders](https://github.com/microsoft/recommenders)** — best-practice implementations + evaluation (collaborative filtering, ALS, SAR…); the reference library

## Reinforcement Learning Environments
- [AirSim (Microsoft)](https://github.com/microsoft/AirSim) — autonomous vehicle simulator on Unreal/Unity → see [[modules/robotics/index]]
- [RLTrader](https://github.com/notadamking/RLTrader) — crypto trading gym environment → see [[modules/quant-finance/applications-of-quantitative-finance]]
- [SafetyGym (OpenAI)](https://openai.com/blog/safety-gym/) — RL with safety constraints

## AutoML / Novelty
- **[AutoML Zero](https://github.com/google-research/google-research/tree/master/automl_zero)** — evolutionary search discovering ML algorithms from basic math ops only

## Feature Engineering
- [Featuretools](https://www.featuretools.com/) — automated feature engineering (Deep Feature Synthesis)

## Related Pages

- [[modules/data-science/index|Data Science Hub]] · [[python-datascience-frameworks]] — tools these topics run on
- [[modules/ai/sub-notes/MODULE_2_PROBLEM_SOLVING_SEARCH|Module 2 — Search]] · [[modules/ai/AI_MASTER_NOTES|AI Master Notes]] — coursework-side theory
- [[curated-reading-list]] — CV/DL essays from the reading archive