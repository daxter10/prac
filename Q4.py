import numpy as np
import matplotlib.pyplot as plt
# Define the function f(x)
def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x
# Generate x values
x = np.linspace(-5, 5, 20)
print(x)

y = objective_function(x)
print(y)

plt.plot(x, y, label='f(x) = -10Cos(pi x - 2.2) + (x + 1.5) * x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(' Function f(x)')
plt.grid(True)

min_y = min(y)
min_x = x[np.argmin(y)]
plt.scatter(min_x, min_y, color='blue', label=f'Minimum: ({min_x}, {min_y})')

plt.legend()
plt.show()

print("Global optimal solution is", min_x)
print("Optimal function value is", min_y)
