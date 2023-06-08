n=int(input())
for i in range(1,n+1):
    s=""
    d=""
    h=" "*(n-i)
    for j in range(1,i+1):
        s=s+str(j)
    for k in range(1,i):
        d=str(k)+d
    print(h+s+d)
        