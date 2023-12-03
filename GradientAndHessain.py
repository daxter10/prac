import sympy as sp

x1, x2 = sp.symbols('x1 x2')
function = 100*(x2-x1**2)**2 + (1-x1)**2
gradient = [sp.diff(function,x1),sp.diff(function,x2)]
hessian = [[sp.diff(gradient[0],x1), sp.diff(gradient[0],x2)],[sp.diff(gradient[1],x1),sp.diff(gradient[1],x2)]]

print("Gradient: ")
print(gradient)
print("\nHessian: ")
print(hessian)