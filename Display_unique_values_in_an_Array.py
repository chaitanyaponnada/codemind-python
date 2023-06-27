n=int(input())
a=list(map(int,input().split()))
l=[]
s=set(a)
# print(s)

d=[]
for i in s:
    c=0
    i=int(i)
    for j in a:
        j=int(j)
        if(i==j):
            c=c+1
    if(c==1):
        d.append(i)
z=len(d)
if(z==0):
    print(-1)
else:
    for i in d:
        print(i,end=" ")

        
    