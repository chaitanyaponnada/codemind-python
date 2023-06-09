n=int(input())
a=list(map(int,input().split()))
z=len(a)

for i in a:
    c=0
    for j in range(z):
        if(i>a[j]):
            c=c+1
    print(c,end=" ")