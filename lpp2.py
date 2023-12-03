import pulp
import matplotlib.pyplot as plt

lp_problem = pulp.LpProblem("LPP", pulp.LpMaximize)

x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

lp_problem += 3 * x + 2 * y

lp_problem += x <= 4
lp_problem += y <= 6
lp_problem += 2 * x + y <= 12

lp_problem.solve()

print("Status:", pulp.LpStatus[lp_problem.status])

print("x =", x.varValue)
print("y =", y.varValue)

print("Optimal Value =", pulp.value(lp_problem.objective))


plt.plot(x.varValue, y.varValue, 'ro', label="Optimal Value")
plt.fill([0, 4, 4, 3, 0], [0, 0, 4, 6, 6], 'b', alpha=0.2)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphical Solution of LPP")

plt.legend()

plt.grid(True)
plt.show()
