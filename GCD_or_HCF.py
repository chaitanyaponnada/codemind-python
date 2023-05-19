a,b=map(int,input().split())

if a>b:
    gcd=b
else:
    gcd=a
    
s=gcd
for i in range(1,s+1):
    if(a%i==0 and b%i==0):
        s=i
print(s)