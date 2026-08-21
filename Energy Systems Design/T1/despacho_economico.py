"""
Trabalho 1 - Despacho Economico Simplificado
Disciplina: Projeto em Sistemas de Energia II (EEL7833)
UFSC - 2026.2

Resolve o problema de programacao linear e plota a regiao viavel.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# ============================================================
# DADOS DO PROBLEMA
# ============================================================
c1 = 150  # Custo variavel G1 (R$/MWh)
c2 = 220  # Custo variavel G2 (R$/MWh)
g1_max = 80  # Capacidade maxima G1 (MW)
g2_max = 70  # Capacidade maxima G2 (MW)
demanda = 100  # Demanda minima (MW)
reserva = 10  # Reserva minima (MW)
cap_total = g1_max + g2_max  # 150 MW
gen_max = cap_total - reserva  # 140 MW (limite por reserva)

# ============================================================
# RESOLUCAO COM SCIPY (PROGRAMACAO LINEAR)
# ============================================================
# min Z = 150*g1 + 220*g2
# Restricoes no formato: A_ub @ x <= b_ub e A_eq @ x = b_eq
# scipy.linprog so aceita <= , entao multiplicamos >= por -1

# -g1 - g2 <= -100  (demanda: g1 + g2 >= 100)
#  g1 + g2 <= 140   (reserva)
A_ub = [[-1, -1],
        [1, 1]]
b_ub = [-demanda, gen_max]

# Limites das variaveis
bounds = [(0, g1_max), (0, g2_max)]

# Coeficientes da funcao objetivo
c = [c1, c2]

# Resolver
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

print("=" * 50)
print("DESPACHO ECONOMICO SIMPLIFICADO - SOLUCAO OTIMA")
print("=" * 50)
print(f"Geracao G1:        {result.x[0]:.1f} MW")
print(f"Geracao G2:        {result.x[1]:.1f} MW")
print(f"Geracao total:     {result.x[0] + result.x[1]:.1f} MW")
print(f"Reserva disponivel:{cap_total - (result.x[0] + result.x[1]):.1f} MW")
print(f"Custo total:       {result.fun:.2f} R$/h")
print("=" * 50)

# ============================================================
# AVALIACAO DOS VERTICES
# ============================================================
vertices = {
    'A': (30, 70),
    'B': (70, 70),
    'C': (80, 60),
    'D': (80, 20),
}

print("\nAVALIACAO DOS VERTICES:")
print(f"{'Vertice':<10}{'g1 (MW)':<10}{'g2 (MW)':<10}{'Z (R$/h)':<12}")
print("-" * 42)
for nome, (g1, g2) in vertices.items():
    z = c1 * g1 + c2 * g2
    print(f"{nome:<10}{g1:<10}{g2:<10}{z:<12.2f}")

# ============================================================
# GRAFICO DA REGIAO VIAVEL
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(9, 7))

# Eixos
g1_range = np.linspace(0, 100, 500)

# Restricoes (linhas)
# g1 + g2 = 100 -> g2 = 100 - g1
g2_demanda = 100 - g1_range
# g1 + g2 = 140 -> g2 = 140 - g1
g2_reserva = 140 - g1_range

# Plotar restricoes
ax.plot(g1_range, g2_demanda, 'b-', linewidth=1.5, label=r'$g_1 + g_2 = 100$ (demanda)')
ax.plot(g1_range, g2_reserva, 'r-', linewidth=1.5, label=r'$g_1 + g_2 = 140$ (reserva)')
ax.axvline(x=g1_max, color='green', linestyle='-', linewidth=1.5, label=r'$g_1 = 80$')
ax.axhline(y=g2_max, color='purple', linestyle='-', linewidth=1.5, label=r'$g_2 = 70$')

# Regiao viavel (preenchida)
# Vertices em ordem: A(30,70) -> B(70,70) -> C(80,60) -> D(80,20) -> A
vertices_plot = np.array([[30, 70], [70, 70], [80, 60], [80, 20], [30, 70]])
ax.fill(vertices_plot[:, 0], vertices_plot[:, 1], alpha=0.2, color='cyan', label='Regiao viavel')

# Marcar vertices
for nome, (g1, g2) in vertices.items():
    z = c1 * g1 + c2 * g2
    ax.plot(g1, g2, 'ko', markersize=7)
    ax.annotate(f'{nome} ({g1}, {g2})\nZ = {z:.0f}',
                xy=(g1, g2), xytext=(g1 + 2, g2 + 3),
                fontsize=9, ha='left')

# Marcar solucao otima
ax.plot(result.x[0], result.x[1], 'r*', markersize=18, zorder=5, label='Solucao otima')

# Curvas de nivel da funcao objetivo (isocustos)
g1_grid, g2_grid = np.meshgrid(np.linspace(0, 100, 200), np.linspace(0, 90, 200))
Z_grid = c1 * g1_grid + c2 * g2_grid
levels = [14000, 16400, 19000, 22000, 25000]
cs = ax.contour(g1_grid, g2_grid, Z_grid, levels=levels, colors='gray',
                linestyles='dashed', linewidths=0.8, alpha=0.6)
ax.clabel(cs, fmt='%.0f R$', fontsize=8)

# Formatacao
ax.set_xlim(-5, 105)
ax.set_ylim(-5, 90)
ax.set_xlabel(r'$g_1$ (MW) - Geracao G1', fontsize=12)
ax.set_ylabel(r'$g_2$ (MW) - Geracao G2', fontsize=12)
ax.set_title('Despacho Economico Simplificado\nRegiao Viavel e Solucao Otima', fontsize=13)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('regiao_viavel.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nGrafico salvo em 'regiao_viavel.png'")
