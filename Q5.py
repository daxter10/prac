import numpy as np
from scipy.optimize import differential_evolution

def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x


bounds = [(-10, 10)]  


result = differential_evolution(objective_function, bounds)


min_x = result.x
global_min_val = result.fun

print("global min x: ",min_x)
print("Global Optimal Solution:")
print(f"x = {min_x[0]}")
print(f"f(x) = {global_min_val}")
