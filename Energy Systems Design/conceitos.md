# Energy Systems Design - Key Concepts

Core concepts from my Energy Systems Design course (EEL7833) at UFSC. The course focuses on computational projects applied to planning and scheduling the operation of electric power systems.

---

## 1. Mathematical Optimization Fundamentals

Every energy systems problem can be framed as an optimization problem:

- **Decision variables:** what we control (e.g., how much to generate, how much water to turbine)
- **Objective function:** what we want to minimize/maximize (e.g., minimize total operating cost)
- **Constraints:** physical and operational limits (e.g., reservoir capacity, generation limits, demand balance)
- **Feasible set:** all solutions that satisfy the constraints
- **Optimal solution:** the feasible solution that best satisfies the objective

Linear Programming (LP) is the starting point — problems where objective and constraints are all linear.

---

## 2. The Brazilian Power System (SIN)

- Brazil's grid is the **Sistema Interligado Nacional (SIN)** — one of the largest interconnected systems in the world
- Generation mix is heavily **hydroelectric** (~60%), complemented by thermal, wind, and solar
- Hydro plants are organized in **cascades** along river basins — upstream decisions affect downstream plants
- The system requires **real-time balance** between generation and demand at all times
- Planning happens at multiple time horizons: long-term (years), medium-term (months), short-term (days/hours)

---

## 3. Hydroelectric Plant Modeling

A hydro plant converts the potential energy of stored water into electricity:

**Key components:**
- Reservoir (stores water, has volume limits)
- Generating units (turbines + generators)
- Spillway (releases excess water without generating)

**Water balance equation:**

> V(t+1) = V(t) + Inflow(t) - Turbined(t) - Spilled(t)

**From water to power:**
- **Gross head** = upstream level - downstream level
- **Net head** = gross head - hydraulic losses
- **Power** = efficiency * density * gravity * net head * turbined flow
- Efficiency depends on flow, head, and unit characteristics

**Operational constraints:**
- Min/max reservoir volume
- Min/max turbined flow (engulfment limits)
- Forbidden operating zones
- Number of units online affects total production

---

## 4. Hydroelectric Production Function

The production function maps (turbined flow, head) → electrical power output.

- It's **nonlinear** (depends on flow, head, and efficiency curves)
- For optimization, we approximate it using **piecewise linear functions** (planes/cuts)
- More units online = more total capacity but different efficiency profile
- The approximation quality depends on the discretization grid

**Why it matters:** LP solvers need linear constraints, so we linearize the production function to use it in optimization models.

---

## 5. Intertemporal Operation and the Value of Water

This is the fundamental dilemma of hydro-dominated systems:

> "Should I use the water now or save it for later?"

- **Immediate cost:** using water now avoids burning expensive thermal fuel today
- **Future cost:** if you use too much water now, you may need expensive thermal generation later
- **Opportunity cost:** the value of storing water = the future savings it enables
- **Value of water:** the economic signal that balances present and future costs

**Key insight:** Decisions are **coupled in time** — today's turbining changes tomorrow's reservoir level, which changes future generation capacity.

A myopic strategy (use all water now) can be much worse than one that considers the full planning horizon.

---

## 6. Thermal Power Plant Modeling

Thermal plants burn fuel to generate electricity. They are more expensive but more controllable:

- **Variable costs:** proportional to generation (fuel consumption curves)
- **Startup/shutdown costs:** turning a unit on or off is expensive
- **Generation limits:** min/max power when online
- **Ramp constraints:** max rate of increase/decrease in generation
- **Minimum up/down times:** once started, must stay on for X hours; once stopped, must stay off for Y hours
- **Binary decisions:** unit is either ON or OFF (introduces integer variables)

**Merit order dispatch:** rank units by variable cost, dispatch cheapest first until demand is met.

---

## 7. Renewable Generation and Uncertainty

Wind and hydro inflows are **stochastic** — we can't predict them exactly:

**Wind power:**
- Power depends on wind speed (cubic relationship in the useful range)
- Cut-in speed (minimum to generate), rated speed (full power), cut-out speed (shut down for safety)
- Modeled with autoregressive processes

**Hydro inflows:**
- Modeled as stochastic processes (historical data + statistical models)
- High variability between wet and dry seasons

**Propagation of uncertainty:** uncertain inputs → uncertain generation → uncertain costs and feasibility

---

## 8. Daily Operation Scheduling (Unit Commitment)

The integrated problem that ties everything together:

1. Discretize the day into time stages (e.g., hourly)
2. For each stage: determine hydro generation (volumes, flows, heads, production function)
3. Simulate wind generation (from scenarios)
4. Calculate residual demand (total demand - wind - hydro)
5. Schedule thermal units to cover residual demand (respecting all constraints)
6. Compute total costs (variable + startup + emergency generation)
7. Analyze results: costs, resource utilization, constraint satisfaction

**The challenge:** integrating all models (hydro nonlinearities, thermal integer decisions, wind uncertainty) into a single coherent optimization or simulation framework.

---

## 9. Key Trade-offs in Power System Operation

| Trade-off | Description |
|-----------|-------------|
| Water now vs later | Use hydro today (cheap) vs save for uncertain future |
| Cost vs reliability | Minimum cost dispatch vs maintaining reserves |
| Thermal flexibility vs cost | More units online = more flexible but higher fixed costs |
| Model detail vs tractability | More accurate models are harder to solve |
| Deterministic vs stochastic | Ignoring uncertainty is simpler but riskier |

---

*This document will be updated as the course progresses.*
