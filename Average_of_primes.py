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
l=[]
for i in a:
    if(prime(i)):
        l.append(i)
print(format(sum(l)/len(l),'.2f'))