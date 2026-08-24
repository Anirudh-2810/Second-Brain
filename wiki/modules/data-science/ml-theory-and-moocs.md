---
course_code: "DATA-SCI"
course_name: "Data Science & Machine Learning Field"
unit: "Module 2 — ML Theory, Courses & MOOCs"
tags: [machine-learning, deep-learning, moocs, fastai, stanford, gradient-descent, cnn, gan, learning-resources]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#machine-learning-theory"
---

## For future agent
ML/DL theory resources and the major MOOC catalog from the knowledge repo. Answers "which course should I take" and "where's the canonical explanation of X concept." Course links are 2020-era but the canonical ones (fast.ai, CS231n, D2L) are actively maintained as of 2026 (high confidence).

# Machine Learning Theory & Courses

## Canonical References

| Resource | Why It Matters |
|----------|---------------|
| [Deep Learning Book](http://www.deeplearningbook.org/) | THE graduate text (Goodfellow/Bengio/Courville): NN → autoencoders → representation learning |
| [Dive into Deep Learning (D2L)](https://d2l.ai/) | Theory AND practice in runnable code; Berkeley-backed, interactive notebooks |
| [PRML Code Examples](https://github.com/ctgk/PRML) | Python implementations of Bishop's *Pattern Recognition and Machine Learning* |
| [Google ML Glossary](https://developers.google.com/machine-learning/glossary/) | Quick definitions lookup |
| [Most Cited DL Papers](https://github.com/terryum/awesome-deep-learning-papers) | The historical canon, ranked by citations |
| [Papers With Code SOTA](https://paperswithcode.com/sota) | State-of-the-art results + implementations, browsable by task |
| [Overview of Gradient Descent (Ruder)](http://sebastianruder.com/optimizing-gradient-descent/) | SGD variants explained: momentum, AdaGrad, RMSprop, Adam |
| [Precision & Recall](https://www.wikiwand.com/en/Precision_and_recall) | The core evaluation metrics, precisely defined |
| [Google AI Education](https://ai.google/education/) | Google's own learn-from-experts portal |

## Course Catalog (pick ONE primary)

### Top Tier (start-here candidates)
- **[fast.ai — Practical Deep Learning for Coders](http://www.fast.ai/)** — top-down: train real models day one; philosophy: "making neural nets uncool again"
- **[Dive into Deep Learning](https://d2l.ai/)** — bottom-up with math + code together; best if you want depth
- **[Stanford CS231n — CNNs for Visual Recognition](http://cs231n.stanford.edu/)** — the classic computer vision course
- **[mlcourse.ai](https://github.com/Yorko/mlcourse.ai)** — open ML course: trees, boosting, feature engineering, unsupervised — **no deep learning**, perfect classical-ML complement to fast.ai

### Specialized / Supporting
- [Stanford CS221 — AI](http://web.stanford.edu/class/cs221/) — broad AI (search, logic, planning)
- [Stanford CS224d — Deep Learning for NLP](http://cs224d.stanford.edu/)
- [Harvard CS109 — Data Science](http://cs109.github.io/2015/) — classic DS course (pandas, sklearn, viz)
- [Coursera Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning) — Andrew Ng, deeplearning.ai
- [Coursera TensorFlow in Practice](https://www.coursera.org/specializations/tensorflow-in-practice)
- [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course/) — genuinely crash-paced
- [Udacity Deep Learning (Google)](https://de.udacity.com/course/deep-learning--ud730)
- [Full Stack Deep Learning](https://course.fullstackdeeplearning.com/) — training model → deployed AI system (production gap)
- [MIT Computational Thinking + 3blue1brown](https://www.youtube.com/playlist?list=PLP8iPy9hna6Q2Kr16aWPOKE0dz9OnsnIJ) — math/CV/Julia
- [Machine Learning Mastery](https://machinelearningmastery.com/) — recipe-style tutorials

## Core Concept Explanations

### Neural Networks & Deep Learning
- **[A Recipe for Training Neural Networks (Karpathy)](http://karpathy.github.io/2019/04/25/recipe/)** — the debugging/training discipline: overfit one batch first, then scale. Essential.
- **[Deep Learning in Neural Networks: Overview (Schmidhuber)](https://www.sciencedirect.com/science/article/pii/S0893608014002135)** — comprehensive survey (paywall)

### CNNs
- ["Best explanation of CNN on the internet" (Medium)](https://medium.com/technologymadeeasy/the-best-explanation-of-convolutional-neural-networks-on-the-internet-fbb8b1ad5df8)
- [Beginner's Guide to CNNs (Adeleshpande)](https://adeshpande3.github.io/adeshpande3.github.io/A-Beginner's-Guide-To-Understanding-Convolutional-Neural-Networks/)
- **[CNN Explainer (interactive)](https://github.com/poloclub/cnn-explainer)** — visual, in-browser layer-by-layer

### Generative Adversarial Networks
- [deeplearning4j GAN introduction](https://getpocket.com/a/read/1994338110)

### Classical Algorithms
- Logistic Regression: [Data Science Simplified Pt 11](https://towardsdatascience.com/data-science-simplified-part-11-logistic-regression-5ae8d994bf0e); [Instrumental Variables thinking (Shakir Mohamed)](http://blog.shakirm.com/2018/10/machine-learning-trick-of-the-day-8-instrumental-thinking/)
- Decision Trees: [Random Forests for complete beginners (victorzhou)](https://victorzhou.com/blog/intro-to-random-forests/)
- Unsupervised on mixed data: [r/datascience thread](https://www.reddit.com/r/datascience/comments/7e4o9s/what_are_good_approaches_for_unsupervised/)
- Imbalanced classes: **[Undersampling/Oversampling + proper CV (Marco Altini)](https://www.marcoaltini.com/blog/dealing-with-imbalanced-data-undersampling-oversampling-and-proper-cross-validation)** — key point: resample inside CV folds only
- Meta-learning: [Unsupervised Meta-Learning for Few-Shot Classification (arXiv 1803.00676)](https://arxiv.org/abs/1803.00676)
- NLP overview: [How to Solve 90% of NLP Problems (Insight)](https://blog.insightdatascience.com/how-to-solve-90-of-nlp-problems-a-step-by-step-guide-fda605278e4e); [EFF AI Progress Metrics](https://www.eff.org/ai/metrics)

## Interview Prep
- [Data Science Interview Questions (grigorev)](https://github.com/alexeygrigorev/data-science-interviews) — with answers
- [160 Data Science Interview Questions (hackernoon)](https://hackernoon.com/160-data-science-interview-questions-415s3y2a)

## Related Pages

- [[modules/data-science/index|Data Science Hub]] · [[roadmaps-and-study-guides]] — where courses fit in a full path
- [[python-datascience-frameworks]] — implementing what you learn here
- [[modules/ai/index|AI Module Hub]] — vault coursework notes (PEAS, search, fuzzy logic…)
- [[modules/programming/math-for-programming|Math for Programming]] — prerequisite math mindset