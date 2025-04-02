import sympy as sp

var_name = sp.Symbol("x")
f = var_name**2
y = sp.diff(f,var_name)

print(y)