import numpy as np 

A = np.array([[2, 1], [1, 2]]) 
x = np.array([[1, 1]]).T 

tol = 1e-6
max_iter = 100
lam_prev = 0
  
for i in range(max_iter): 
    x1 = A @ x / np.linalg.norm(x) 
    lam = (x.T @ A @ x) / (x.T @ x) 
  
    if np.abs(lam - lam_prev) < tol: 
        break
 
    lam_prev = lam 
  
print(float(lam)) 
print(x)