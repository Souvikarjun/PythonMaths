first_num = 7
mod = 13
multi = 5
i=1
inverse = []
while i < mod:
    if(i*first_num)%mod == 1:
       inverse.append(i)
    
    i = i+1
x=[]    
for j in inverse:
    x.append(multi*j)

print("the answere of x =", x)