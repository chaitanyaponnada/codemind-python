n=int(input())
a=0
b=1
print(a,end=" ")
print(b,end=" ")
while(n-2!=0):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    n=n-1