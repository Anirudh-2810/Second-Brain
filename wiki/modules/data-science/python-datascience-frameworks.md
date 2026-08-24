---
course_code: "DATA-SCI"
course_name: "Data Science & Machine Learning Field"
unit: "Module 3 — Python for Data Science: Frameworks"
tags: [python, data-science, pandas, sklearn, xgboost, lightgbm, catboost, tensorflow, keras, pytorch, learning-resources]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#python-for-data-science-by-framework"
---

## For future agent
The Python ML stack organized by framework: classical (pandas/sklearn/boosting) and deep learning (TensorFlow 2/Keras, PyTorch). The TF section is unusually deep (training, tuning, TensorBoard, inference, migration). Use when choosing a library or debugging inside one. TF-specific links are 2020-era; core APIs stable as of 2026.

# Python for Data Science — By Framework

## Foundation Stack

### pandas / scikit-learn / Basics
- **[Python Data Science Handbook (jakevdp)](https://github.com/jakevdp/PythonDataScienceHandbook)** — the free book covering NumPy/pandas/matplotlib/sklearn; the foundation
- [Missing Data & Imputation in pandas](https://pandas.pydata.org/pandas-docs/stable/missing_data.html)
- [Cross-Validation in sklearn](http://scikit-learn.org/stable/modules/cross_validation.html)
- [auto-sklearn](https://automl.github.io/auto-sklearn/stable/) — automated model selection + hyperparameters on sklearn
- [Vaex out-of-core DataFrames](https://towardsdatascience.com/vaex-out-of-core-dataframes-for-python-and-fast-visualization-12c102db044a) — bigger-than-RAM dataframes

### Gradient Boosting (the tabular-data workhorse)
| Library | Notes | Key Link |
|---------|-------|----------|
| **XGBoost** | The original boosted-trees winner | [Introduction to Boosted Trees](http://xgboost.readthedocs.io/en/latest/model.html) |
| **LightGBM** (Microsoft) | Fast, distributed GBT/GBDT/MART | [github.com/microsoft/LightGBM](https://github.com/microsoft/LightGBM) |
| **CatBoost** (Yandex) | Gradient boosting w/ categorical features native; CPU+GPU | [github.com/catboost/catboost](https://github.com/catboost/catboost) |
| xgboost bagging example | Text classification use-case | [tradeshift-text-classification](https://github.com/daxiongshu/tradeshift-text-classification) |

## TensorFlow 2.x & Keras (deep section)

### Learn
- **[eat TensorFlow 2 in 30 days](https://github.com/lyhue1991/eat_tensorflow2_in_30_days)** — digestible tf2 book + study plan incl. in-depth mechanics
- [TensorFlow Book (BinRoot)](https://github.com/BinRoot/TensorFlow-Book)
- [Official TF ML Curriculum](https://www.tensorflow.org/resources/learn-ml)
- [TensorFlow Developer Certificate](https://www.tensorflow.org/certificate)
- [Inside TensorFlow (Yelp engineering)](https://engineeringblog.yelp.com/2019/11/inside-tensorflow.html) — internals tour
- [LSTM recipe generation walkthrough](https://github.com/trekhleb/machine-learning-experiments/blob/master/assets/recipes_generation.en.md) — end-to-end LSTM training guide

### Training Mechanics
- [Learning Rate Schedules & Decay](https://www.pyimagesearch.com/2019/07/22/keras-learning-rate-schedules-and-decay/)
- Hyperparameter optimization:
  - [keras-tuner](https://keras-team.github.io/keras-tuner/#keras-tuner-documentation)
  - [hyperas](https://github.com/maxpumperla/hyperas) — hyperopt wrapper for keras prototyping
  - [AutoKeras](https://autokeras.com/) — AutoML on Keras
- TensorBoard:
  - [Distributions & histograms with fit_generator](https://stackoverflow.com/questions/42425858/tensorboard-distributions-and-histograms-with-keras-and-fit-generator)
  - [Showing all images in TensorBoard](https://stackoverflow.com/questions/45584557/how-to-show-all-my-images-in-tensorboard)

### Data Ingest & Migration
- [Train-test split with ImageDataGenerator](https://stackoverflow.com/questions/42443936/keras-split-train-test-set-when-using-imagedatagenerator)
- [TF 1.X → 2.X: AutoGraph & eager mode](https://medium.com/ai%C2%B3-theory-practice-business/tensorflow-1-0-vs-2-0-part-1-computational-graphs-4bb6e31c1a0f)
- [Effective TensorFlow 2 (official)](https://www.tensorflow.org/guide/effective_tf2)

### Inference Performance
- [CPU inference via Intel MKL](https://software.intel.com/content/www/us/en/develop/articles/maximize-tensorflow-performance-on-cpu-considerations-and-recommendations-for-inference.html)

### Frameworks & DSL Extensions
- [Ludwig (Uber)](https://github.com/uber/ludwig) — train/test DL models without writing code
- [TF-Coder](https://blog.tensorflow.org/2020/08/introducing-tensorflow-coder-tool.html) — generates TF expressions from input/output examples
- **[Einops](https://github.com/arogozhnikov/einops)** — readable tensor ops DSL across numpy/pytorch/tf; widely adopted since

### NLP in TF
- [CNN for text classification (Kim 2014 impl.)](https://github.com/dennybritz/cnn-text-classification-tf)
- [word2vec tutorial (official)](https://www.tensorflow.org/tutorials/word2vec)
- [wildml CNN text classification](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/#more-452)

### Object Detection
- [Real-time hand detector (SSD, Egohands)](https://towardsdatascience.com/how-to-build-a-real-time-hand-detector-using-neural-networks-ssd-on-tensorflow-d6bac0e4b2ce) · [code](https://github.com/victordibia/handtracking)

## Keras (standalone era — still relevant API patterns)

- **[Deep Learning with Python (Chollet)](https://www.manning.com/books/deep-learning-with-python)** · [notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks)
- [Official examples library](https://github.com/keras-team/keras/tree/master/examples)
- [scikit-learn API wrapper](https://keras.io/scikit-learn-api/)
- Advanced GitHub issues worth reading (architectural nuances):
  - [Combining filter lengths in 1D conv layers](https://github.com/keras-team/keras/issues/1023) · [Dynamic k-max pooling](https://github.com/keras-team/keras/issues/373) · [Non-static CNN (Kim 2014)](https://github.com/keras-team/keras/issues/1515) · [Extracting feature weights](https://github.com/keras-team/keras/issues/12) · [2D vs 1D convolutions for text](https://github.com/keras-team/keras/issues/233) · [Word vectors instead of Embedding layer](https://github.com/keras-team/keras/issues/853) · [MNIST transfer learning](https://github.com/keras-team/keras/blob/master/examples/mnist_transfer_cnn.py)

## PyTorch
- [torch2rt (NVIDIA)](https://github.com/NVIDIA-AI-IOT/torch2trt) — PyTorch → TensorRT conversion for inference speed
- [TorchCV](https://github.com/donnyyou/torchcv) — PyTorch CV framework
- [BoTorch](https://github.com/pytorch/botorch) — Bayesian optimization built on PyTorch

## Related Pages

- [[modules/data-science/index|Data Science Hub]] · [[ml-theory-and-moocs]] — theory behind these tools
- [[python-datascience-topics]] — applying frameworks to problem types
- [[mlops-production-deployment]] — shipping these models
- [[modules/object-oriented-programming/overview|OOP in Python]] — reading framework source effectively