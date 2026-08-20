# Plano de Ensino - EEL7833/EEL7848 Projeto em Sistemas de Energia II

**Professor:** Erlon Cristian Finardi  
**Codigo:** EEL7833 (Nivel I) / EEL7848 (Nivel II)  
**Carga horaria:** 4h semanais (72h total) - Teoricas  
**Curso:** Engenharia Eletrica (202)  
**Pre-requisito:** EEL7071 Introducao a Sistemas de Energia Eletrica  
**Periodo:** 12/08/2026 a 09/12/2026

---

## Ementa

Desenvolvimento de projetos computacionais aplicados ao planejamento e programacao da operacao de sistemas de energia eletrica. Fundamentos de modelagem matematica e otimizacao. Representacao matematica da producao, transporte e consumo de energia eletrica (hidreletricas, termeletricas, eolicas). Modelagem da funcao de producao hidreletrica, balanco hidrico, valor da agua. Modelagem de custos e restricoes de termeletricas. Representacao de incertezas. Programacao diaria da operacao.

---

## Objetivos

Ao final, o aluno devera ser capaz de:

- Formular problemas de otimizacao (variaveis de decisao, funcao objetivo, restricoes)
- Implementar modelos computacionais de otimizacao e simulacao
- Representar operacao de usinas hidreletricas (balanco hidrico, cotas, quedas, rendimentos)
- Construir aproximacoes lineares por partes da funcao de producao hidreletrica
- Compreender operacao hidrotermica e conceito de valor da agua
- Modelar custos e restricoes de usinas termeletricas
- Representar geracao renovavel variavel e incertezas
- Integrar geracao hidro + termo + eolica + demanda em programacao diaria
- Analisar resultados com criterios tecnicos e economicos

---

## Conteudo Programatico

### 1. Fundamentos de modelagem e otimizacao
- Variaveis de decisao, funcao objetivo, restricoes
- Programacao Linear, solucao grafica
- Implementacao computacional

### 2. Industria de energia eletrica
- Sistema Interligado Nacional (SIN)
- Fontes de geracao e matriz eletrica brasileira
- Planejamento e programacao da operacao

### 3. Representacao da producao, transporte e consumo
- Recursos de geracao em problemas de planejamento
- Curvas de carga e demanda residual
- Modelo de barra unica, intercambios

### 4. Modelagem de usinas hidreletricas
- Reservatorio, unidades geradoras, vertedouro
- Balanco hidrico, volumes, vazoes
- Cotas, queda bruta, perdas hidraulicas, queda liquida
- Rendimentos e potencia eletrica produzida
- Limites de engolimento, faixas operativas

### 5. Funcao de producao hidreletrica
- Funcao de producao individual e agregada
- Representacao nao linear
- Aproximacoes lineares por partes (planos/cortes)

### 6. Operacao intertemporal e valor da agua
- Acoplamento temporal das decisoes
- Custo imediato vs custo futuro
- Custo de oportunidade da geracao hidreletrica
- Problemas hidrotermicos em multiplos estagios

### 7. Usinas termeletricas
- Custos variaveis, fixos, partida/parada
- Limites de geracao, rampas
- Tempos minimos de operacao/desligamento
- Despacho por ordem de merito

### 8. Geracao renovavel e incertezas
- Geracao eolica (velocidade do vento vs potencia)
- Modelos autorregressivos
- Afluencias hidrologicas estocasticas
- Propagacao de incertezas

### 9. Programacao diaria integrada
- Horizonte diario discretizado em estagios
- Integracao hidro + termo + eolica + demanda
- Custos totais, restricoes, analise de resultados

---

## Avaliacoes

| Trabalho | Tema | Entrega |
|----------|------|---------|
| T1 | Problema introdutorio de otimizacao | 19/08 |
| T2 | Funcao de producao hidreletrica e configuracoes operativas | 09/09 |
| T3 | Aproximacao linear por partes da funcao de producao | 30/09 |
| T4 | Balanco hidrico, operacao intertemporal e valor da agua | 21/10 |
| T5 | Programacao de termeletricas (custos e restricoes) | 11/11 |
| T6 | **Trabalho integrador** - Programacao diaria completa | 09/12 |

**Calculo da media:**
- MT = (T1 + T2 + T3 + T4 + T5) / 5
- **MS = 0.40 * MT + 0.60 * T6**
- Aprovacao: MS >= 6.0, frequencia >= 75%, T6 entregue, minimo 4 de 5 trabalhos entregues, MT >= 4.0

---

## Cronograma Resumido

| Semana | Data | Conteudo |
|--------|------|----------|
| 1 | 12/08 | Apresentacao, fundamentos otimizacao, inicio T1 |
| 2 | 19/08 | Desenvolvimento e entrega T1, divulgacao T2 |
| 3 | 26/08 | Demanda, geracao, componentes hidreletricas, inicio T2 |
| 4 | 02/09 | Balanco hidrico, volumes, cotas, quedas, rendimentos |
| 5 | 09/09 | Configuracoes de unidades, entrega T2, divulgacao T3 |
| 6 | 16/09 | Funcao de producao hidreletrica, inicio T3 |
| 7 | 23/09 | Aproximacoes lineares por partes |
| 8 | 30/09 | Validacao da aproximacao, entrega T3, divulgacao T4 |
| 9 | 07/10 | Operacao intertemporal, valor da agua, inicio T4 |
| 10 | 14/10 | Balanco hidrico intertemporal, valor terminal |
| 11 | 21/10 | Cenarios de afluencia, entrega T4, divulgacao T5 |
| 12 | 28/10 | Termeletricas: custos, estados, inicio T5 |
| 13 | 04/11 | Rampas, tempos minimos, despacho por merito |
| 14 | 11/11 | Entrega T5, divulgacao T6, intro topicos 8 e 9 |
| 15 | 18/11 | T6: organizacao dados, integracao inicial |
| 16 | 25/11 | T6: modelo integrado |
| 17 | 02/12 | T6: cenarios, validacao, relatorio |
| 18 | 09/12 | Entrega final T6, arguicao |

---

## Bibliografia Basica

1. Silva, E.L. Formacao de Precos em Mercados de Energia. Sagra Luzatto, 2012.
2. Larroyd, P.V. Otimizacao Estocastica no Planejamento Hidrotermico. Tese UFSC, 2016.
3. Fortunato et al. Introducao ao Planejamento da Expansao e Operacao de Sistemas de Energia. UFF, 1990.
4. Wood, Wollenberg, Sheble. Power Generation, Operation, and Control. 2013.
5. Portal CCEE - https://ccee.micropower.com.br
