def prime(n):
    if(n==1):
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
                break
        return True

n=int(input())
l=[]
res=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
for i in l:
    if(prime(i)==False):
        res.append(i)
print(len(res))