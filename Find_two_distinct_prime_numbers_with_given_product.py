def prime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
            break
    return True



n=int(input())
l=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(int(i))

p=[]
for i in l:
    if(prime(i)):
        p.append(i)
        
for i in p:
    z=False
    for j in p:
        if(int(i)*int(j)==n):
            z=True
    if(z==True):
        print(i,j)
        break    
else:
    print(-1)



