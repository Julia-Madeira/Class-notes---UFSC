# Learning Hub

My space for organizing everything I'm learning — from university courses (Electrical Engineering at UFSC) to personal projects and self-study. The goal is simple: **be more organized**, document what I learn, and build things along the way using AI to help me accelerate, experiment, and turn ideas into reality faster.

---

## Why this exists

I wanted a system where I could:
- Organize lecture notes, exercises, and materials by course
- Document personal projects related to what I'm studying
- Look back and see what I actually learned (not just what I attended)
- Share key concepts and project write-ups publicly
- Build a habit of learning consistently, inside and outside the classroom

---

## Courses

| Course | Code | Status |
|--------|------|--------|
| Aprendizado de Maquina | MTM3587 | In progress |

## Projects

| Project | Related to | Status |
|---------|-----------|--------|
| *Coming soon* | — | — |

---

## Key Learnings

Things that clicked, ideas worth remembering, and concepts I don't want to forget.

### Aprendizado de Maquina

- **The full ML pipeline matters more than any single algorithm.** Data acquisition, preprocessing, feature extraction, train/val/test split, choosing H, defining the loss, training, and evaluating generalization — each step can make or break your model.

- **You can't just minimize training error.** The generalization bound R(f) <= R_emp(f) + complexity(H) means that a model too complex will "memorize" the training data but fail on new data. This is overfitting, and it's the fundamental tension in ML.

- **Choosing the hypothesis class H is a design decision, not a formality.** Too simple = underfitting (can't capture patterns). Too complex = overfitting (captures noise). The sweet spot depends on your data and the problem.

---

## Structure

```
Class-notes---UFSC/
├── README.md
├── .gitignore
├── Aprendizado de maquina/
│   └── conceitos.md    (key concepts - public)
├── ... (more courses to come)
└── ... (personal projects to come)
```

Each course has a `conceitos.md` file with the most important concepts explained clearly. Projects get their own folders with write-ups. Everything else (detailed lecture notes, exercises, syllabi, PDFs) stays local and private.

---

## Tools

- **Kiro** as my AI-powered notebook (takes notes in real-time during lectures)
- **Markdown** for everything (lightweight, version-controlled, readable)
- **Git/GitHub** to track progress and never lose anything

---

*Last updated: August 19, 2026*
