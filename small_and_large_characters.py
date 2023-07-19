n=input().split()
for i in n:
    a=sorted(str(i))
    x=a[0]
    z=len(a)
    y=a[z-1]
    x=str(x)
    y=str(y)
    print(x,y,end=" ")