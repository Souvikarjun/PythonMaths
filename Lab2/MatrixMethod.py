def linearWithMatrix(a1,a2,a3,b1,b2,b3):
    det_A = (a1*b2 - a2*b1)
    if det_A != 0:
        inverse_A = [[b2/det_A,-b1/det_A],[-a2/det_A,a1/det_A]]
        x1 = inverse_A[0][0]*a3 + inverse_A[0][1]*b3
        x2 = inverse_A[1][0]*a3 + inverse_A[1][1]*b3
        return x1,x2
    else:
        print("There is no unique Solution")

result = linearWithMatrix(1,1,3,1,-1,1)
if result != None:
    print(result)