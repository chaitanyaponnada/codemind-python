n=int(input())
a=input().split()
c=0
m=0
for i in a:
    i=str(i)
    if(i=="1"):
        c=c+1
    else:
        c=0
    if c>m:
        m= c
print(m)