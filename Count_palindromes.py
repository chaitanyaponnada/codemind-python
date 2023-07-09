def pal(n):
    if(n==n[::-1]):
        return True
    else:
        return False

n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    i=str(i)
    if(pal(i)):
        c=c+1
print(c)