n=int(input())
for i in range(n):
    a=int(input())
    p=1
    while(a!=1):
        p=p*a
        a=a-1
    print(p)