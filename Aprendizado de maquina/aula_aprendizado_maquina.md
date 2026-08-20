# Aprendizado de Maquina - Anotacoes de Aula

**Data:** 19/08/2026  
**Curso:** UFSC  
**Abordagem:** Vies matematico (nao engenharia)  
**Codigo:** MTM3587  
**Pagina do curso:** [mtm.ufsc.br/~douglas/26.2/mtm3587](http://mtm.ufsc.br/~douglas/26.2/mtm3587)

**Horario de atendimento:** Quarta-feira, 15:30 - 17:00 | Sala MTM 210

---

## Bibliografia

| # | Livro | Foco |
|---|-------|------|
| 1 | **Mathematics for Machine Learning** (Deisenroth, Faisal & Ong) | **Principal** - especialmente a Parte II |
| 2 | The Elements of Statistical Learning (Hastie, Tibshirani & Friedman) | Referencia complementar |
| 3 | Understanding Machine Learning: From Theory to Algorithms (Shalev-Shwartz & Ben-David) | Teoria de aprendizado |
| 4 | Elementos da Teoria de Aprendizagem de Maquina Supervisionada (V. Pestov) | Avancado - alem do escopo do curso |

> **Nota:** O foco principal sera no livro "Mathematics for Machine Learning", Parte II, que cobre:
> - Cap 8: Quando modelos encontram dados (problema de otimizacao)
> - Cap 9: Regressao Linear
> - Cap 10: Reducao de Dimensionalidade com PCA
> - Cap 11: Estimacao de Densidade e Modelos de Mistura Gaussiana (GMM)
> - Cap 12: Classificacao com Maquinas de Vetores de Suporte (SVM)
>
> A Parte I do mesmo livro traz os fundamentos matematicos (algebra linear, geometria analitica, decomposicao de matrizes, calculo vetorial, probabilidade e otimizacao) que serao a base para entender os algoritmos.

---

## Avaliacoes

| Avaliacao | Data |
|-----------|------|
| Prova 1 | 23/09/2026 |
| Prova 2 | 04/11/2026 |
| Prova 3 | 02/12/2026 |
| Recuperacao | 09/12/2026 |

**Composicao da nota:**
- **75%** Provas
- **25%** Atividades de laboratorio

---

## Topicos da Aula

### Aula 1 - 19/08/2026: Introducao

#### Tipos de Problemas em Aprendizado de Maquina

- **Regressao:** prever um valor continuo (ex: prever temperatura, preco de imovel)
- **Classificacao:** prever uma categoria/classe discreta (ex: spam ou nao-spam, sorrindo ou nao)

#### Exemplo Pratico: Detectar se uma pessoa esta sorrindo

**Problema:** Dada uma imagem de um rosto, classificar se a pessoa esta sorrindo ou nao (classificacao binaria).

**Pipeline de resolucao:**

1. **Aquisicao de dados brutos**
   - Coletar imagens de rostos (sorrindo e nao sorrindo)

2. **Pre-processamento dos dados**
   - Centralizar rostos nas imagens
   - Normalizar iluminacao, tamanho, etc.

3. **Feature Extraction (Extracao de caracteristicas)**
   - Transformar a imagem em um vetor de atributos numericos relevantes
   - Exemplos de features:
     - Distancia da orelha ate a ponta da boca
     - Tamanho/largura da boca (aumenta ao sorrir)
     - Curvatura dos labios
   - O objetivo e capturar o que muda entre "sorrindo" e "nao sorrindo"

4. **Preparacao dos conjuntos de dados**
   - **Treino:** usado para ajustar o modelo
   - **Validacao:** usado para escolher hiperparametros e evitar overfitting
   - **Teste:** avaliacao final (dados nunca vistos pelo modelo)

5. **Determinar a classe de modelos H (hipotese)**
   - Escolher o espaco de funcoes H onde o modelo f sera buscado
   - f pertence a H (f in H)
   - Exemplos: regressao logistica, SVM, redes neurais, arvores de decisao...
   - A escolha de H define a "capacidade" do modelo (trade-off bias-variancia)

6. **Definir uma funcao de perda (loss function)**
   - Mede o quao bem o modelo f ajusta os dados de treino
   - Propriedade: **l(f(xi), yi) >= 0** (perda e sempre nao-negativa)
   - Exemplo: **l(f(xi), yi) = (f(xi) - yi)^2** (erro quadratico)
   - Outros exemplos:
     - Classificacao: erro 0-1, cross-entropy
     - Regressao: erro quadratico medio (MSE), erro absoluto (MAE)
   - E essa funcao que sera minimizada no processo de treinamento (otimizacao)

7. **Treinamento / Ajuste de parametros: Escolher f in H que minimiza o Risco Empirico**
   - **Risco Empirico (Empirical Risk):**
     - R_emp(f) = (1/n) * sum_{i=1}^{n} l(f(xi), yi)
   - Ou seja: e a media das perdas sobre todos os n exemplos de treino
   - O objetivo do treinamento e encontrar f* = argmin_{f in H} R_emp(f)
   - Intuitivamente: entre todas as funcoes possiveis em H, escolher a que erra menos nos dados de treino

> **Cuidado:** Minimizar apenas o risco empirico pode levar a **overfitting** (o modelo decora os dados de treino mas nao generaliza). Por isso existem tecnicas de regularizacao e o uso do conjunto de validacao.

8. **Erro de generalizacao**
   - E o erro esperado do modelo em dados novos (nao usados no treino)
   - Risco real: R(f) = E[ l(f(x), y) ] (esperanca sobre a distribuicao real dos dados)
   - O que queremos de verdade e minimizar R(f), nao apenas R_emp(f)
   - A diferenca entre o risco empirico e o risco real e o **gap de generalizacao**
   - Avaliar no conjunto de teste e uma estimativa do erro de generalizacao

#### Relacao entre Risco Empirico e Risco Real (bound de generalizacao)

- **Risco Empirico** R_emp(f): media das perdas nos dados de **treino** (observavel)
- **Risco Real** R(f): erro esperado em dados **novos** (o que queremos minimizar, mas nao observamos diretamente)

**Desigualdade fundamental:**

> **R(f) <= R_emp(f) + termo_de_complexidade(H)**

- O risco real e limitado pelo risco empirico + um termo que cresce com a complexidade de H
- Se H e muito complexo: R_emp(f) pode ir a zero (decora os dados), mas o termo de complexidade explode → overfitting
- Se H e muito simples: termo de complexidade e pequeno, mas R_emp(f) ja e alto → underfitting
- **Conclusao:** nao adianta zerar o risco empirico se a complexidade do modelo for muito alta, pois o risco real sera grande

> **Intuitivamente:** quanto mais "poderosa" a classe de modelos, mais facil e decorar os dados de treino, mas mais dificil e garantir que o modelo generaliza. O bound formaliza esse trade-off.

---

### Conceitos Fundamentais: Overfitting e Underfitting

**Overfitting (sobreajuste):**
- O modelo se ajusta **demais** aos dados de treino, "decorando" inclusive o ruido e particularidades daquele conjunto especifico
- Resultado: erro de treino muito baixo, mas erro de generalizacao (teste) alto
- O modelo nao consegue generalizar para dados novos
- Sintoma: grande diferenca entre R_emp(f) (baixo) e R(f) (alto)
- Causas comuns: modelo muito complexo (H muito grande), poucos dados de treino, treinar por tempo demais
- Analogia: estudante que decora as respostas da prova anterior mas nao entende a materia

**Underfitting (subajuste):**
- O modelo e **simples demais** para capturar os padroes reais dos dados
- Resultado: erro alto tanto no treino quanto no teste
- O modelo nao consegue representar a relacao entre entradas e saidas
- Sintoma: R_emp(f) ja e alto (o modelo erra ate nos dados de treino)
- Causas comuns: modelo muito simples (H muito restrito), features insuficientes, treinar por pouco tempo
- Analogia: tentar ajustar uma reta a dados que seguem uma curva

> **Resumo visual:**
> - Underfitting: modelo simples demais → erro alto em tudo
> - Bom ajuste: equilibrio entre complexidade e generalizacao
> - Overfitting: modelo complexo demais → "decora" o treino, falha no teste
>
> O objetivo e encontrar o ponto ideal de complexidade do modelo (trade-off bias-variancia).

> **Conceito importante:** O pipeline acima e generico para problemas de aprendizado supervisionado. A qualidade das features extraidas e a escolha adequada de H sao decisivos para o desempenho do modelo.

---
