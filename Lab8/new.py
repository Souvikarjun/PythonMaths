import sympy as sp

A = [[22,77,11],[33,23,89],[55,100,100]]
A1 = sp.Matrix(A)

Det_A1 = sp.det(A1)

sp.pprint(A1)
print(Det_A1)
