def pal(n):
    n=str(n)
    n=n.lower()
    return n==n[::-1]
    
n=input().split()
c=0
for i in n:
    if(pal(i)):
        c=c+1
print(c)