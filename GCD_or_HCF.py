a,b=map(int,input().split())
if(a>b):
    m=a
else:
    m=b
gcd=m
for i in range(1,a*b+1):
    if(a%i==0 and b%i==0):
        gcd=i
print(gcd)        