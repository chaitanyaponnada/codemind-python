n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if(i==0):
        a.append(i)
    else:
        b.append(i)
z=b+a
for i in z:
    print(i,end=" ")