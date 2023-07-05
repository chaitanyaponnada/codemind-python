n=int(input())
m=input()
s=0
for i in range(n):
    a=list(map(int,input().split()))
    z=sum(a)
    s=s+z
print(s)