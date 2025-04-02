import sympy as sp

x,y = sp.symbols('x y')

f1 = y*(x**2)
f2 = x*sp.sin(y)

F = (f1, f2)

F_matrix = [[sp.diff(f1,x), sp.diff(f1,y)], [sp.diff(f2,x), sp.diff(f2,y)]]

F_matrix = sp.Matrix(F_matrix)


sp.pprint(F_matrix)