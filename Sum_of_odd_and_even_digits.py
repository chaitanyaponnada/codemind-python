n=int(input())
a=list(map(int,input().split()))
l=[]
d=[]
z=len(a)
for i in range(z):
    if(i%2==0):
        l.append(a[i])
    else:
        d.append(a[i])
s1=sum(l)
s2=sum(d)
r=s1-s2
if(r==0):
    print("YES")
else:
    print("NO")