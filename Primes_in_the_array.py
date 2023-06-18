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
z=list(map(int,input().split()))
l=[]
for i in z:
    q=prime(i)
    l.append(q)
c=0
for j in l:
    if(j==True):
        c=c+1
print(c)
