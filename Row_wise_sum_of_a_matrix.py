a,b=map(int,input().split())
for i in range(a):
    s=0
    a=input().split()
    a=list(a)
    for j in a:
        j=int(j)
        s=s+j
    print(s,end=" ")