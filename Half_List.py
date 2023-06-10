n=int(input())
a=list(map(int,input().split()))
z=n//2
s=""
for j in range(n-1,z-1,-1):
    print(a[j],end=" ")
for i in range(0,z):
    print(a[i],end=" ")
