import sympy as sp

varName = sp.Symbol("x")

y = (varName**3) - (3*varName**2) + 6

firstDiff = sp.diff(y, varName)

CriticalPoints = sp.solve(firstDiff, varName)

secondDiff = sp.diff(firstDiff, varName)

for i in CriticalPoints:
    result = secondDiff.subs(varName, i)
    print(i)
    if result>0:
        print("minimum = ", i)
    elif result<0:
        print("maximum = ", i)
    else:
        print("not defined")
