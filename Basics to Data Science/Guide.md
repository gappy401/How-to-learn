# 130+ Key Concepts to Know for Data Science / ML Interviews 
*Updated for the 2025–2026 landscape*

**Core pillars:** Statistics · Machine Learning · Coding (Python, R) · SQL · LLMs/GenAI · MLOps · Causal Inference · Experimentation · System Design


## Statistics

### Basic Statistical Concepts
- Univariate statistics — mean, median, mode
- Standard deviation and variance
- Covariance and correlation
- Population and sample
- Nominal, ordinal, continuous, discrete data types
- P-value & significance level
- Simpson's Paradox
- Selection bias

### Hypothesis Testing
- Hypothesis statements (null vs. alternative)
- Z-test
- T-test
- T-test for sample means
- Z-test for proportions
- Paired and unpaired t-tests
- Variance test
- ANOVA
- Chi-squared test
- Goodness of fit test for categorical data
- Pairwise tests
- T-test assumptions
- Non-parametric tests
- Type 1 & Type 2 errors

### Probability & Distributions
- Bayes' Theorem
- Conditional probability
- Normal distribution
- Uniform distribution
- Bernoulli distribution
- Binomial distribution
- Geometric distribution
- Poisson distribution
- Exponential distribution
- Deriving the mean and variance of distributions
- Central Limit Theorem
- The Birthday problem
- Card probability problems
- Die roll problems

### Regression Modeling
- OLS regression
- Confidence vs. prediction intervals
- Logistic regression
- Regression model assumptions
- Model diagnostic checks
- R-squared vs. adjusted R-squared
- AIC, BIC, Cp statistics
- Model interpretation

---

## Causal Inference *(new)*
- Correlation vs. causation
- Confounders, mediators, colliders
- Propensity score matching
- Difference-in-differences
- Instrumental variables (conceptual)
- Causal graphs / DAGs basics

## Experimentation & A/B Testing *(new / expanded)*
- Power analysis & sample size calculation
- Novelty effects and network effects
- Multiple testing correction (Bonferroni, FDR)
- Sequential testing / the peeking problem
- Guardrail metrics vs. primary metrics

---

## Machine Learning

### ML Foundations
- Bias & variance trade-off
- Predictability vs. interpretability trade-off
- Feature selection
- Feature engineering
- Model validation
- Curse of dimensionality
- Data leakage
- Classification problems
- Regression problems

### ML Algorithms
- Regularized regression
- Decision tree
- Random forest
- XGBoost
- Bagging vs. boosting
- Variable importance from tree models
- Principal Component Analysis (PCA)
- Hyperparameter tuning
- K-means clustering
- Hierarchical clustering
- The elbow technique
- Neural networks
- Cross-validation
- AUC vs. accuracy
- Imbalanced class problem

### Deep Learning Fundamentals *(new)*
- Gradient descent variants (SGD, Adam)
- Backpropagation intuition
- Overfitting prevention (dropout, batch norm, early stopping)
- CNN / RNN basics

### LLMs & Generative AI *(new — biggest gap in older lists)*
- Transformer architecture basics (attention, embeddings, tokenization)
- Prompt engineering fundamentals
- RAG (retrieval-augmented generation) — how it works, when to use vs. fine-tuning
- Fine-tuning vs. few-shot vs. zero-shot
- Embedding models & vector databases (cosine similarity, ANN search)
- LLM evaluation (perplexity, BLEU/ROUGE limitations, LLM-as-judge, hallucination detection)
- Context windows, temperature, top-k / top-p sampling

### Responsible AI / Ethics *(new)*
- Fairness metrics (demographic parity, equalized odds)
- Model explainability (SHAP, LIME)
- Bias in training data

---

## Productionization & MLOps *(expanded)*
- Model checks
- Model productionization steps
- Online model evaluation
- Designing scalable model systems
- Model monitoring & drift detection (data drift vs. concept drift)
- Feature stores
- A/B testing infrastructure for ML (shadow deployment, canary releases)
- Model versioning & reproducibility
- Batch vs. real-time inference trade-offs
- CI/CD for ML pipelines
- Model serving (latency/throughput trade-offs, quantization basics)

## ML System Design *(new — increasingly its own interview category)*
- End-to-end ML system design (e.g., "design a recommendation system")
- Cold start problem
- Online vs. offline evaluation gap

## Data Engineering Adjacent *(new)*
- ETL vs. ELT
- Data quality checks / schema validation
- Basics of distributed compute (what Spark does, why it matters)
- Streaming vs. batch processing

---

## Algorithms & Data Structures
- Array problems
- Math problems
- String problems
- Matrix problems
- Palindrome
- Rotate a matrix by 180 degrees

---

## SQL

### Data Manipulation
- Calculate using statistical functions
- Aggregation
- Lags
- Group By
- Filtering
- JOINs
- Sorting

### Clauses & Concepts
- SELECT
- DISTINCT
- ORDER BY
- ALIAS
- WHERE
- NULL
- Aggregations (SUM, MIN, MAX, COUNT, AVG)
- HAVING
- JOINs
- SETs
- Subqueries
- PARTITION BY
- RANK
- CASE

---

## How to Use This List
- **Data Scientist roles**: weight heavily toward Statistics, Causal Inference, Experimentation, and Regression Modeling.
- **ML Engineer roles**: weight heavily toward Deep Learning, LLMs/GenAI, MLOps, and ML System Design.
- **Applied Scientist roles**: expect a blend, with more depth in ML Algorithms and LLMs.
- SQL and Algorithms/Data Structures are near-universal regardless of track.

*Want this broken into a role-specific study plan (DS vs. MLE vs. Applied Scientist) or turned into a Word doc / spreadsheet checklist? Just ask.*
