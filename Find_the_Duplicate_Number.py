n=int(input())
a=list(map(int,input().split()))
b=set(a)
for i in b:
    c=0
    for j in a:
        if(i==j):
            c=c+1
    if(c>=2):
        print(i)
    