# UFSC - Study Hub

My digital notebook for the Mathematics degree at UFSC (2026.2). The goal here is simple: **be more organized**, keep everything in one place, and actually track what I need to do instead of letting things pile up.

---

## Why this exists

I wanted a system where I could:
- Have all my lecture notes, exercises, and materials organized by course
- Keep track of deadlines, exams, and to-dos
- Look back and see what I actually learned (not just what I attended)
- Build a habit of reviewing and studying consistently

---

## Courses

| Course | Code | Status |
|--------|------|--------|
| Aprendizado de Maquina | MTM3587 | In progress |

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
UFSC-materias/
├── README.md
├── .gitignore
├── Aprendizado de maquina/
│   ├── aula_aprendizado_maquina.md    (lecture notes)
│   ├── exercicios_aula1_ML.md         (exercises & study guide)
│   └── plano_ensino_aprendizado_maquina.md (syllabus summary)
└── ... (more courses to come)
```

---

## Tools

- **Kiro** as my AI-powered notebook (takes notes in real-time during lectures)
- **Markdown** for everything (lightweight, version-controlled, readable)
- **Git/GitHub** to track progress and never lose anything

---

*Last updated: August 19, 2026*
