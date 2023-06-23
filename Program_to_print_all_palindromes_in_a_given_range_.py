def pal(n):
    n=str(n)
    a=n[::-1]
    if(n==a):
        return True
    else:
        return False

a=int(input())
b=int(input())
for i in range(a,b+1):
    if(pal(i)):
        print(i,end=" ")