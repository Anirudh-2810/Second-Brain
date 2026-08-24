---
course_code: "DATA-SCI"
course_name: "Data Science & Machine Learning Field"
unit: "Module 12 — Curated Reading List (Distilled)"
tags: [reading-list, essays, articles, machine-learning, career, python, data-engineering, deep-learning]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#reading-list"
---

## For future agent
The knowledge repo's unsorted ~250-link reading list + read archive, distilled into thematic clusters. Only high-signal items are listed; dead/irrelevant links (device tips, forum one-offs) were dropped during ingestion. This is the essay-depth layer — individual pages in this module are the reference layer.

# Curated Reading List — By Theme

## Machine Learning Practice & Career
- **[A Recipe for Training Neural Networks (Karpathy)](http://karpathy.github.io/2019/04/25/recipe/**)** *(also in [[ml-theory-and-moocs]])* — training discipline
- [Software 2.0 (Karpathy)](https://medium.com/@karpathy/software-2-0-a64152b37c35) — the paradigm essay: code written by optimization
- [Top 6 errors novice ML engineers make](https://medium.com/towards-data-science/top-6-errors-novice-machine-learning-engineers-make-e82273d394db)
- [Essential algorithms every ML engineer needs to know](https://towardsdatascience.com/essential-algorithms-every-ml-engineer-needs-to-know-3167b1e940f)
- [Which ML algorithm for which problem (kdnuggets)](https://www.kdnuggets.com/2017/11/machine-learning-algorithms-choose-your-problem.html)
- [Regularization explained](https://towardsdatascience.com/regularization-in-machine-learning-76441ddcf99a)
- [Becoming an MLE Step 2: pick a process](https://medium.com/towards-data-science/becoming-a-machine-learning-engineer-step-2-pick-a-process-942eef6ba8dd)
- [What I learned from Kaggle contests (freecodecamp)](https://medium.freecodecamp.org/what-i-learned-from-kaggle-contests-d3123e17a36b)
- [Building a DS portfolio blog (Dataquest)](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/)
- Interview war story: [5 companies in 5 days, 5 offers](https://medium.com/@XiaohanZeng/i-interviewed-at-five-top-companies-in-silicon-valley-in-five-days-and-luckily-got-five-job-offers-25178cf74e0f)

## Deep Learning Concepts
- [Feature Visualization (Distill)](https://distill.pub/2017/feature-visualization/) — what CNN layers learn; Distill quality bar
- [How to Use t-SNE Effectively (Distill)](https://distill.pub/2016/misread-tsne/) — parameter traps in the standard viz tool
- [Visualizing MNIST (colah)](http://colah.github.io/posts/2014-10-Visualizing-MNIST/) — dimensionality reduction intuition
- [Batch normalization explained](https://medium.com/towards-data-science/batch-normalization-in-neural-networks-1ac91516821c)
- Capsule networks: [Hinton's CapsNets Pt I: intuition](https://medium.com/@pechyonkin/understanding-hintons-capsule-networks-part-i-intuition-b4b559d1159b) · [What is a CapsNet](https://hackernoon.com/what-is-a-capsnet-or-capsule-network-2bfbe48769cc)
- Theory: [New theory cracks open the black box of deep learning (Quanta)](https://www.quantamagazine.org/new-theory-cracks-open-the-black-box-of-deep-learning-20170921/)
- Counterpoint: [The impossibility of intelligence explosion (Chollet)](https://medium.com/@francois.chollet/the-impossibility-of-intelligence-explosion-5be4a9eda6ec)
- [Population-based training of neural nets (DeepMind)](https://deepmind.com/blog/population-based-training-neural-networks/)
- [Applied DL Part 3: autoencoders](https://medium.com/towards-data-science/applied-deep-learning-part-3-autoencoders-1c083af4d798)
- Free book-tier: [Neural Networks and Deep Learning (Nielsen)](http://neuralnetworksanddeeplearning.com/chap1.html)

## Computer Vision
- **[Object detection: overview in the age of DL (Tryolabs)](https://tryolabs.com/blog/2017/08/30/object-detection-an-overview-in-the-age-of-deep-learning)** + [comprehensive review](https://medium.com/towards-data-science/deep-learning-for-object-detection-a-comprehensive-review-73930816d8d9)
- [A Year in Computer Vision (M Tank)](http://www.themtank.org/a-year-in-computer-vision) — annual survey
- Production cases: [Dropbox OCR pipeline](https://blogs.dropbox.com/tech/2017/04/creating-a-modern-ocr-pipeline-using-computer-vision-and-deep-learning/) · [Dropbox document scanning](https://blogs.dropbox.com/tech/2016/08/fast-and-accurate-document-detection-for-scanning/) · [Apple on-device face detection](https://machinelearning.apple.com/2017/11/16/face-detection.html)
- [Number plate recognition with TF (Matthew Earl)](https://matthewearl.github.io/2016/05/06/cnn-anpr/)
- [Data augmentation techniques in CNN/TensorFlow](https://medium.com/ymedialabs-innovation/data-augmentation-techniques-in-cnn-using-tensorflow-371ae43d5be9)
- Browser pose estimation: [TF.js real-time human pose](https://medium.com/tensorflow/real-time-human-pose-estimation-in-the-browser-with-tensorflow-js-7dd0bc881cd5)

## NLP & Text
- **[Stop Using word2vec (Stitch Fix)](http://multithreaded.stitchfix.com/blog/2017/10/18/stop-using-word2vec/)** — production reality check on embeddings
- [word2vec tutorial (Rare Technologies)](https://rare-technologies.com/word2vec-tutorial/)
- [Essential NLP guide: top 10 tasks with code (Analytics Vidhya)](https://www.analyticsvidhya.com/blog/2017/10/essential-nlp-guide-data-scientists-top-10-nlp-tasks/)
- [Text classification with NLTK + sklearn (bbengfort)](https://bbengfort.github.io/tutorials/2016/05/19/text-classification-nltk-sckit-learn.html)
- Topic modeling: [complete guide (nlpforhackers)](https://nlpforhackers.io/topic-modeling/) · [NLTK+Gensim walkthrough](https://towardsdatascience.com/topic-modelling-in-python-with-nltk-and-gensim-4ef03213cd21)
- [tf-idf analysis in sklearn (buhrmann)](https://buhrmann.github.io/tfidf-analysis.html) · [fast keyword ID via tfidf+wikipedia](https://hackernoon.com/the-fastest-way-to-identify-keywords-in-news-articles-tfidf-with-wikipedia-python-version-baf874d7eb16)
- [Clean text for ML (ML Mastery)](https://machinelearningmastery.com/clean-text-machine-learning-python/)
- NLP guide (tomassetti): [A Guide to Natural Language Processing](https://tomassetti.me/guide-natural-language-processing/)
- [Natural language generation at Google Research](https://medium.com/towards-data-science/natural-language-generation-at-google-research-bbf2c3756d80)

## Python Craft
- **[Improve Your Python: Unit Testing (Jeff Knupp)](https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/)** · [Classes & OOP (Knupp)](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
- [OOP with TDD example pt 1 (Digital Cat)](http://blog.thedigitalcatonline.com/blog/2015/05/13/python-oop-tdd-example-part1/)
- [Custom scikit-learn estimators](http://danielhnyk.cz/creating-your-own-estimator-scikit-learn/) · [SO version w/ CV](https://stackoverflow.com/questions/20330445/how-to-write-a-custom-estimator-in-sklearn-and-use-cross-validation-on-it)
- Pandas: **[Optimizing pandas code for speed](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6)** · [Seven clean reshape steps](https://towardsdatascience.com/seven-clean-steps-to-reshape-your-data-with-pandas-or-how-i-use-python-where-excel-fails-62061f86ef9c) · [How to learn pandas (Petrou)](https://towardsdatascience.com/how-to-learn-pandas-108905ab4955)
- Conda workflows: [My Python env workflow with conda](https://tdhopper.com/blog/my-python-environment-workflow-with-conda/) · [Anaconda Project](https://github.com/Anaconda-Platform/anaconda-project)
- [Run-time method patching (Tryolabs)](https://tryolabs.com/blog/2013/07/05/run-time-method-patching-python/)
- Lambda deep-dive: [Yet another lambda tutorial](https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/) · [language-agnostic SO answer](https://stackoverflow.com/questions/16501/what-is-a-lambda-function)
- Scraping: [intro (datawhatnow)](https://datawhatnow.com/introduction-web-scraping-python/) · [mastering scraping (hackernoon)](https://hackernoon.com/mastering-python-web-scraping-get-your-data-back-e9a5cc653d88) · [building datasets with Scrapy](https://medium.com/towards-data-science/using-scrapy-to-build-your-own-dataset-64ea2d7d4673)

## Data Engineering & Infra
- **[Beginner's Guide to Data Engineering Pt 1 (kdnuggets)](https://www.kdnuggets.com/2018/01/beginners-guide-data-engineering-1.html)**
- [Kafka in Python (Adnan Siddiqi)](http://blog.adnansiddiqi.me/getting-started-with-apache-kafka-in-python/)
- [Data science at the command line (free book)](https://www.datascienceatthecommandline.com/)
- Docker: [Jupyter container walkthrough](https://tsaprailis.com/2017/10/10/Docker-for-data-science-part-1-building-jupyter-container/) · [simplified docker-ing](https://becominghuman.ai/docker-for-data-science-part-1-dd41e5ef1d80) · [Docker with R (DevOps view)](https://www.r-bloggers.com/why-use-docker-with-r-a-devops-perspective/)
- [Pachyderm — reproducible pipelines](http://pachyderm.io/) · [Airbnb Scaling Knowledge](https://medium.com/airbnb-engineering/scaling-knowledge-at-airbnb-875d73eff091) · [DS maturity model (Domino)](https://blog.dominodatalab.com/introducing-the-data-science-maturity-model/)
- Time-series DBs: [top 10 open-source roundup](https://blog.outlyer.com/top10-open-source-time-series-databases)
- Data lakes primer: [relevance in big data community](https://blog.rakam.io/data-lakes-a-sneak-peek-into-their-relevance-in-the-big-data-community-f3841e948dc1)
- Startup infra: [choice of datastore mistakes](https://www.stavros.io/posts/startup-mistakes-datastore/)
- Cloud notebooks: [Jupyter on GCP in 15 min](https://medium.com/towards-data-science/running-jupyter-notebook-in-google-cloud-platform-in-15-min-61e16da34d52) · [Colaboratory](https://research.google.com/colaboratory/unregistered.html)

## Statistics & Methods
- Test vs validation set: **[stats.SE canonical answer](https://stats.stackexchange.com/questions/19048/what-is-the-difference-between-test-set-and-validation-set)**
- k-fold CV in NNs: [SO walkthrough](https://stackoverflow.com/questions/25889637/how-to-use-k-fold-cross-validation-in-a-neural-network)
- PCA do's/don'ts: [the dos and don'ts of PCA](https://medium.com/@sadatnazrul/the-dos-and-donts-of-principal-component-analysis-7c2e9dc8cc48)
- SVM intuition pt 2: [geometric understanding](https://medium.com/towards-data-science/support-vector-machines-intuitive-understanding-part-2-1046dd449c59)
- Feature selection: [three effective strategies](https://medium.com/towards-data-science/three-effective-feature-selection-strategies-e1f86f331fb1)
- A/B testing interview questions: [Quora thread](https://www.quora.com/What-kind-of-A/B-testing-questions-should-I-expect-in-a-data-scientist-interview-and-how-should-I-prepare-for-such-questions)
- Logistic regression coefficients interpretation: [RPubs example](https://rpubs.com/OmaymaS/182726)
- Survey design: [choosing survey methods (UCLA)](http://www.ats.ucla.edu/stat/mult_pkg/faq/svy_howtochoose.htm)

## Trading / Crypto / Quant-Adjacent
- **[Introduction to Learning to Trade with RL (WildML)](http://www.wildml.com/2018/02/introduction-to-learning-to-trade-with-reinforcement-learning/)** → pairs with [[modules/quant-finance/applications-of-quantitative-finance]]
- [Getting started with algorithmic crypto trading (Jay Nagpaul)](https://jaynagpaul.com/algorithmic-crypto-trading)
- [How to make your own trading bot (codeburst)](https://codeburst.io/how-to-make-your-own-trading-bot-83b5c6e35036)
- Crypto rates → Google Sheets: [jbuty how-to](https://jbuty.com/how-to-get-crypto-currencies-rates-and-more-in-google-sheet-1a57e571bc14)
- Bitcoin whitepaper annotated: [Fermat's Library](https://fermatslibrary.com/s/bitcoin) · Ethereum: [smart contracts explained](http://www.gjermundbjaanes.com/understanding-ethereum-smart-contracts/)
- Vault link: [[modules/stock-agent/overview|Stock Agent project]] — this vault's own trading system

## Git & Workflow
- **[Oh shit, git!](http://ohshitgit.com/)** — disaster recovery recipes; bookmark it
- [Five key git concepts explained the hard way (zwischenzugs)](https://zwischenzugs.com/2018/03/14/five-key-git-concepts-explained-the-hard-way/)
- [Syncing a fork (GitHub docs)](https://help.github.com/articles/syncing-a-fork/)
- Code review process keys: [dev.to roundup](https://dev.to/vipinjain/5-keys-to-optimizing-your-code-review-process-341e)
- Open source entry: [First Timers Only](http://www.firsttimersonly.com/) · [CodeTriage](https://www.codetriage.com/)
- tmux minimalism: [guide (HN)](https://news.ycombinator.com/item?id=15776995) · [Medium version](https://medium.com/actualize-network/a-minimalist-guide-to-tmux-13675fb160fa)

## Career, Craft & Mindset
- [Imposter syndrome (Brandon Rohrer)](https://brohrer.github.io/imposter_syndrome.html)
- [The Programmer's Guide to a Sane Workweek (codewithoutrules)](https://codewithoutrules.com/saneworkweek/) · [part-time programming interview](https://codewithoutrules.com/2018/01/08/part-time-programmer/)
- [Code less, think more… incrementally!](https://levelup.gitconnected.com/code-less-think-more-incrementally-98adee22df9b)
- Problem-solving classics: [How to Solve It (Polya)](https://en.wikipedia.org/wiki/How_to_Solve_It) · [How to Solve It by Computer (Dromey)](https://en.wikipedia.org/wiki/How_to_Solve_it_by_Computer)
- Self-taught path threads: [Ask HN: become self-taught SWE](https://news.ycombinator.com/item?id=15946136) · [learned to code, Google interview realities](http://www.reddit.com/r/learnprogramming/comments/7hb7ka/learned_to_code_got_interview_at_google_but_i/) · [Stanford CS9 problem-solving for interviews](https://web.stanford.edu/class/cs9/)
- Soft skills: [softer skills that make you better (dev.to)](https://dev.to/amangautam/softer-skills-that-make-you-a-better-programmer--2g3e) · [active listening technique](https://reddit.com/r/YouShouldKnow/comments/8a9egh/ysk_active_listening_a_technique_developed_by_the/)
- Logbook habit: **[Using a logbook to improve your programming (Routley)](https://routley.io/tech/2017/11/23/logbook.html)** — maps to this vault's daily notes pattern

## Free Book & Resource Aggregators
- [GoalKicker free programming books](http://goalkicker.com/)
- [Free data science books (kdnuggets)](http://www.kdnuggets.com/2015/09/free-data-science-books.html)
- AI cheat-sheet pack: [NN/ML/DL/big data cheat sheets](https://becominghuman.ai/cheat-sheets-for-ai-neural-networks-machine-learning-deep-learning-big-data-678c51b4b463)
- [Stack Overflow Developer Survey 2017](https://insights.stackoverflow.com/survey/2017#technology-languages-over-time) — era snapshot
- [Data Science at Airbnb, Spotify process posts] — org design references (see infra section)

## Read Archive (original repo's archive section, verbatim-worthy)
- [AI chatbot in Python with AIML (DevDungeon)](http://www.devdungeon.com/content/ai-chat-bot-python-aiml)
- [Logbook for programmers (Routley)](https://routley.io/tech/2017/11/23/logbook.html)
- [Optimizing pandas for speed (upside)](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6)
- [The 7 Steps of Machine Learning (TDS)](https://medium.com/towards-data-science/the-7-steps-of-machine-learning-2877d7e5548e)

## Ingestion Notes

- Dropped from source (~60 links): device/setup one-offs, dead forums, non-English pages, duplicate URLs, personal-life bookmarks — no knowledge loss for this vault's purposes
- Several source URLs were malformed (trailing `<`, mismatched anchors); corrected where target was identifiable, otherwise omitted `(TBC)`
- Era caveat stands: 2017–2020 essays; concepts durable, specific tools may be superseded

## Related Pages

- [[modules/data-science/index|Data Science Hub]] — hub; all other pages are this page's reference layer
- [[ml-theory-and-moocs]] · [[python-datascience-topics]] — where these essays' topics get systematic treatment