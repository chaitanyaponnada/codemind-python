n=int(input())
f=0
s=1
print(f,s,end=" ")
while(n-2):
    a=f+s
    print(a,end=" ")
    f=s
    s=a
    n-=1