n=int(input())
a=list(map(int,input().split()))
s=int(input())
l=[]
for i in range(len(a)):
    if(a[i]==s):
        l.append(i)

z=len(l)
if(z==0):
    print(-1,-1)
else:
    print(l[0],l[z-1])
    