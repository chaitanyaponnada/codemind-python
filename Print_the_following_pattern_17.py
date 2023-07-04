n=int(input())
z=n+1
for i in range(n):
    i=i+1
    s=""
    z=int(z)
    z=z-1
    for j in range(n):
        if(j==(i-1) or j==(n-i)):
            s=s+str(z)+" "
        else:
            s=s+" "
    print(s)
