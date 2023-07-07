n=input()
m=set(n)
l=[]
k=[]
n=n.lower()
for i in m:
    c=0
    for j in n:
        if(i==j):
            c=c+1
    if(c<=1):
        l.append(i)
    else:
        k.append(i)
if(len(l)==0):
    print(-1)
else:
    for i in range(len(n)):
        a=n[i]
        if a in l:
            print(i)
            break