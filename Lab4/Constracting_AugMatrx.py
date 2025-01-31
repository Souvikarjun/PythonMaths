import copy
import numpy as np

a = [[1,2,-1],[-2,2,3],[2,0,4]]
b = [[6],[3],[4]]
ab = copy.deepcopy(a)

for i in range(len(a)):
    ab[i].append(b[i][0])

rank_a = np.linalg.matrix_rank(a)   
rank_ab = np.linalg.matrix_rank(ab)   

print(ab)
print(rank_a)
print(rank_ab)

if rank_ab != rank_a:
    print("Got no solutions")

elif rank_ab == rank_a and rank_a == len(a)+1:
    print("Got unique solutions")

else:
    print("Got infinite solutions")
