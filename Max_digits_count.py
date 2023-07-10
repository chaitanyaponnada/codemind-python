n=int(input())
a=list(map(int,input().split()))
m=0
for i in a:
    i=str(i)
    z=len(i)
    if(z>m):
        m=z
l=[]        
for i in a:
    i=str(i)
    if(m==len(i)):
        l.append(i)
print(len(l))