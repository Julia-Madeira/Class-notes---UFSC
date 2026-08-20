# Exercicios e Estudo - Aula 1: Introducao ao Aprendizado de Maquina

**Data da aula:** 19/08/2026  
**Proxima prova:** P1 em 23/09/2026

---

## Topicos para Estudar

### Conceitos fundamentais
- [ ] Diferenca entre regressao e classificacao (exemplos de cada)
- [ ] Tipos de aprendizado: supervisionado, nao-supervisionado, semi-supervisionado, por reforco
- [ ] Pipeline completo de um problema de ML (as 8 etapas vistas em aula)
- [ ] Feature extraction: por que e importante e como features ruins prejudicam o modelo
- [ ] Divisao treino / validacao / teste: por que separar e qual o papel de cada um

### Formalizacao matematica
- [ ] Funcao de perda l(f(x), y): propriedades (nao-negativa), exemplos (erro quadratico, 0-1)
- [ ] Risco empirico: definicao R_emp(f) = (1/n) * sum l(f(xi), yi)
- [ ] Risco real: R(f) = E[l(f(x), y)]
- [ ] Bound de generalizacao: R(f) <= R_emp(f) + complexidade(H)
- [ ] Classe de hipoteses H: o que significa escolher H e como isso afeta o modelo

### Overfitting e Underfitting
- [ ] Definicao precisa de cada um
- [ ] Relacao com a complexidade de H
- [ ] Como o bound de generalizacao explica overfitting
- [ ] Estrategias para combater overfitting (regularizacao, mais dados, modelo mais simples)

### Leitura recomendada
- [ ] Mathematics for Machine Learning (Deisenroth et al.) - Cap 8.1 a 8.3 (quando modelos encontram dados)
- [ ] Understanding Machine Learning (Shalev-Shwartz) - Cap 2 (framework formal de aprendizado)
- [ ] Geron, Maos a obra - Cap 1 (panorama do aprendizado de maquina)

---

## Exercicios Conceituais

### 1. Classificacao vs Regressao
Para cada problema abaixo, diga se e classificacao ou regressao e justifique:
- a) Prever o preco de um imovel a partir de area, numero de quartos e localizacao
- b) Determinar se um e-mail e spam ou nao
- c) Prever a nota de um aluno em uma prova
- d) Diagnosticar se um tumor e benigno ou maligno
- e) Estimar a idade de uma pessoa a partir de uma foto

### 2. Pipeline de ML
Descreva as etapas do pipeline para o seguinte problema: "Classificar digitos escritos a mao (0-9) a partir de imagens 28x28 pixels". Para cada etapa, diga o que voce faria concretamente.

### 3. Funcao de perda
- a) Dado f(x1) = 3.2, y1 = 3.0, f(x2) = 5.1, y2 = 4.0, calcule o risco empirico usando l(f(x),y) = (f(x) - y)^2
- b) Por que a funcao de perda deve ser nao-negativa? O que aconteceria se pudesse ser negativa?
- c) Para um problema de classificacao binaria (y in {0,1}), a perda quadratica e uma boa escolha? Por que?

### 4. Risco empirico vs Risco real
- a) Um modelo tem R_emp = 0.01 no treino mas R = 0.45 no teste. O que esta acontecendo? Como resolver?
- b) Um modelo tem R_emp = 0.40 no treino e R = 0.42 no teste. O que esta acontecendo? Como resolver?
- c) Explique com suas palavras por que minimizar apenas R_emp nao e suficiente.

### 5. Classe de hipoteses H
- a) Se H = {funcoes lineares}, que tipos de relacao o modelo NUNCA vai capturar?
- b) Se H = {todos os polinomios ate grau 100}, qual o risco de usar essa classe com poucos dados?
- c) Explique o trade-off: H pequeno vs H grande.

### 6. Overfitting e Underfitting
Considere um dataset com 20 pontos (x, y) que seguem aproximadamente y = sin(x) + ruido.
- a) Desenhe (ou descreva) o que acontece se ajustarmos um polinomio de grau 1 (reta)
- b) Desenhe (ou descreva) o que acontece se ajustarmos um polinomio de grau 19
- c) Qual grau voce escolheria e por que?

---

## Exercicios Praticos (Python)

### 7. Primeiro contato com Scikit-Learn
```python
# Instale: pip install scikit-learn matplotlib numpy

# a) Carregue o dataset iris do sklearn
# b) Divida em treino (70%) e teste (30%)
# c) Treine um classificador K-NN com k=3
# d) Calcule a acuracia no treino e no teste
# e) Repita com k=1 e k=50. O que muda? Qual sofre overfitting? Qual sofre underfitting?
```

### 8. Visualizando overfitting
```python
# a) Gere 30 pontos: x uniforme em [0, 2*pi], y = sin(x) + ruido gaussiano (std=0.3)
# b) Ajuste polinomios de grau 1, 3, 5, 15 aos dados
# c) Plote cada ajuste junto com os dados
# d) Calcule o erro quadratico medio no treino para cada grau
# e) O que acontece com o erro de treino conforme o grau aumenta?
# f) Gere 30 pontos NOVOS (teste) e calcule o erro em cada modelo. Qual generaliza melhor?
```

---

## Perguntas para Reflexao

1. Por que nao podemos simplesmente usar H = {todas as funcoes possiveis} e garantir R_emp = 0?
2. Se tivessemos infinitos dados de treino, overfitting ainda seria um problema? Por que?
3. Qual a relacao entre o numero de dados n e a complexidade de H que podemos usar?
4. O que acontece com o bound R(f) <= R_emp(f) + complexidade(H) quando n → infinito?

---

## Resumo do que cai na P1 (baseado no plano)

A P1 cobre as semanas 1-5 (Unidade 1 completa + Unidades 2.1 a 2.4):
- Tudo desta aula (conceitos basicos, pipeline, risco empirico/real)
- Naive Bayes e filtro de spam
- Projeto offline de ML ponta a ponta
- Introducao a regressao
- Gradiente descendente
- Modelos lineares regularizados
- Compensacao vies/variancia (bias-variance tradeoff)
