n=int(input())

for i in range(1,n+1):
    s=""
    h=" "*(n-i)
    m=""
    a=65
    b=65
    for j in range(1,i+1):
        s=s+chr(a)
        a=a+1
    for k in range(1,i):
        m=chr(b)+m
        b=b+1
    z=h+s+m
    print(z)
        
        
    