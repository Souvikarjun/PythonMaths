def linearSolution(a1,a2,a3,b1,b2,b3):
    d0 = (a1*b2)-(a2*b1)
    d1 = (a3*b2)-(a2*b3)
    d2 = (a1*b3)-(a3*b1)

    if d0==d1==d2==0:
        print("no solution")
    elif d0 == 0:
        print("Infinite solution")
        return 
    else:
        a = d1/d0
        b = d2/d0
        return a, b
        
    
result = linearSolution(1,2,3,2,4,6)
if result != None:
    print(result)
