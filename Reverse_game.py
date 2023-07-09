def pal(n):
    return n[::-1]

n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    i=str(i)
    l.append(pal(i))
    
for i in l:
    print(int(i),end=" ")