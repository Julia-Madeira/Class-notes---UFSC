# Aprendizado de Maquina - Key Concepts

Core concepts and insights from my Machine Learning course (MTM3587) at UFSC, taught with a mathematical perspective.

---

## 1. The ML Pipeline

A supervised learning problem follows these steps:

1. **Data acquisition** — collect raw data
2. **Preprocessing** — clean, normalize, center (e.g. align faces in images)
3. **Feature extraction** — transform raw data into meaningful numerical attributes
4. **Train / Validation / Test split** — separate data for fitting, tuning, and final evaluation
5. **Choose hypothesis class H** — define the family of models to search over
6. **Define loss function** l(f(x), y) >= 0 — measures how wrong the model is
7. **Training** — find f in H that minimizes empirical risk
8. **Evaluate generalization** — estimate real-world performance on unseen data

---

## 2. Regression vs Classification

| | Regression | Classification |
|---|---|---|
| Output | Continuous value | Discrete category |
| Example | Predict house price | Spam or not spam |
| Loss example | MSE: (f(x) - y)^2 | 0-1 loss, cross-entropy |

---

## 3. Empirical Risk vs True Risk

**Empirical Risk** (what we can compute):

> R_emp(f) = (1/n) * sum_{i=1}^{n} l(f(xi), yi)

**True Risk** (what we actually want to minimize):

> R(f) = E[ l(f(x), y) ]

The goal of training is to find f* = argmin_{f in H} R_emp(f), but what we really care about is R(f).

---

## 4. The Generalization Bound

> **R(f) <= R_emp(f) + complexity(H)**

This is the fundamental inequality of learning theory:
- The true error is bounded by training error + a term that grows with model complexity
- You cannot just memorize the training data (R_emp → 0) because the complexity term explodes
- This formalizes the **bias-variance tradeoff**

---

## 5. Overfitting and Underfitting

**Overfitting:** Model too complex → low training error, high test error. It memorizes noise instead of learning patterns.

**Underfitting:** Model too simple → high training error, high test error. It cannot capture the underlying structure.

The sweet spot is a model complex enough to capture real patterns but simple enough to generalize.

---

## 6. The Hypothesis Class H

Choosing H is a design decision that defines what your model can and cannot learn:
- H = {linear functions} → can only learn linear relationships
- H = {polynomials of degree 100} → can fit anything but will likely overfit
- The right H depends on your data, domain knowledge, and available samples

---

*This document is updated as the course progresses.*
