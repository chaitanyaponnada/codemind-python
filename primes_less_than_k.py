def prime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
            break
    return True

n=int(input())
a=list(map(int,input().split()))
k=int(input())
l=[]
for i in a:
    if(k>=i):
        if(prime(i)):
            l.append(i)
print(len(l))