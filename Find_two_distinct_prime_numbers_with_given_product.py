def prime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
    
n=int(input())
l=[]
for i in range(1,n):
    if(n%i==0):
        l.append(i)

for i in l:
    z=False
    for j in l:
        if((i*j)==n):
            z=True
            break
    if(z==True):
        print(i,j)
        break
else:
    print(-1)