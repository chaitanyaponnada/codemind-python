n,m=map(int,input().split())
l=[]
s=0
for i in range(n):
    a=input().split()
    for i in a:
        i=int(i)
        s=s+int(i)
print(s)