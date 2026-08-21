# Trabalho I - Despacho Economico Simplificado

## Enunciado

Um sistema possui duas unidades geradoras termicas, G1 e G2:
- G1: custo variavel = 150 R$/MWh, capacidade maxima = 80 MW
- G2: custo variavel = 220 R$/MWh, capacidade maxima = 70 MW
- Demanda minima: 100 MW
- Reserva minima de seguranca: 10 MW (no conjunto das duas unidades)

---

## 1. Variaveis de Decisao

- **g1** = potencia gerada pela unidade G1 (em MW)
- **g2** = potencia gerada pela unidade G2 (em MW)

---

## 2. Formulacao do Problema de Programacao Linear

**Funcao objetivo (minimizar custo total):**

> min Z = 150*g1 + 220*g2

**Restricoes:**

| # | Restricao | Significado fisico |
|---|-----------|-------------------|
| R1 | g1 + g2 >= 100 | Atendimento da demanda |
| R2 | g1 + g2 <= 140 | Reserva de seguranca (capacidade total = 150 MW, reserva >= 10 MW, logo geracao <= 150 - 10 = 140 MW) |
| R3 | 0 <= g1 <= 80 | Limites de geracao de G1 |
| R4 | 0 <= g2 <= 70 | Limites de geracao de G2 |

**Nota sobre R2:** A capacidade total instalada e 80 + 70 = 150 MW. Para manter 10 MW de reserva disponivel, a geracao total nao pode exceder 150 - 10 = 140 MW.

---

## 3. Regiao Viavel (descricao para representacao grafica)

A regiao viavel e definida no plano (g1, g2) pelas restricoes:

```
g1 >= 0
g2 >= 0
g1 <= 80
g2 <= 70
g1 + g2 >= 100
g1 + g2 <= 140
```

E um **poligono** no primeiro quadrante, delimitado por:
- Eixos (g1 >= 0, g2 >= 0)
- Linhas verticais (g1 = 80) e horizontais (g2 = 70)
- Reta g1 + g2 = 100 (por baixo)
- Reta g1 + g2 = 140 (por cima)

---

## 4. Vertices da Regiao Viavel

Os vertices sao os pontos de interseccao das restricoes ativas:

| Vertice | g1 | g2 | Como encontrar |
|---------|----|----|----------------|
| A | 30 | 70 | g2 = 70 e g1 + g2 = 100 → g1 = 30 |
| B | 70 | 70 | g2 = 70 e g1 + g2 = 140 → g1 = 70 |
| C | 80 | 60 | g1 = 80 e g1 + g2 = 140 → g2 = 60 |
| D | 80 | 20 | g1 = 80 e g1 + g2 = 100 → g2 = 20 |

**Obs:** Verificar se existe vertice em (80, 70) — neste ponto g1 + g2 = 150 > 140, entao **nao e viavel** (viola a restricao de reserva).

---

## 5. Solucao Otima

Avaliando a funcao objetivo Z = 150*g1 + 220*g2 em cada vertice:

| Vertice | g1 | g2 | Z = 150*g1 + 220*g2 |
|---------|----|----|---------------------|
| A | 30 | 70 | 150(30) + 220(70) = 4.500 + 15.400 = **19.900 R$** |
| B | 70 | 70 | 150(70) + 220(70) = 10.500 + 15.400 = **25.900 R$** |
| C | 80 | 60 | 150(80) + 220(60) = 12.000 + 13.200 = **25.200 R$** |
| D | 80 | 20 | 150(80) + 220(20) = 12.000 + 4.400 = **16.400 R$** |

**Solucao otima: Vertice D → g1 = 80 MW, g2 = 20 MW**

**Custo total minimo: Z* = 16.400 R$/h**

---

## 6. Interpretacao Fisica

- **G1 opera na capacidade maxima (80 MW):** como e a unidade mais barata (150 R$/MWh), o otimo e usa-la ao maximo.
- **G2 opera no minimo necessario (20 MW):** gera apenas o complemento para atender a demanda de 100 MW.
- **Geracao total = 100 MW:** exatamente a demanda minima (restricao ativa).
- **Reserva disponivel = 150 - 100 = 50 MW:** muito acima dos 10 MW exigidos, pois o custo de gerar mais (so para "gastar" reserva) nao faz sentido economicamente.
- **Logica economica:** despacho por **ordem de merito** — a unidade mais barata gera o maximo possivel, a mais cara complementa.

> Este resultado ilustra o principio fundamental do despacho economico: unidades com menor custo variavel sao despachadas prioritariamente.

---

## 7. Resumo

| Grandeza | Valor |
|----------|-------|
| Geracao G1 | 80 MW |
| Geracao G2 | 20 MW |
| Geracao total | 100 MW |
| Reserva disponivel | 50 MW |
| Custo total | 16.400 R$/h |
| Restricoes ativas | g1 = 80 (limite G1) e g1 + g2 = 100 (demanda) |
