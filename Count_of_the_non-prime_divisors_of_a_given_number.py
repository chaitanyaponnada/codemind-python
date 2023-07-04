def prime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
            break
    return True
    
a=int(input())
l=[]
z=[]
for i in range(1,a+1):
    if(a%i==0):
        l.append(i)
        
for j in l:
    if(prime(j)==False):
        z.append(j)
print(len(z))
        