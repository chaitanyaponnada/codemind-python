n=int(input())
l=[]
for i in range(1,n):
    if(n%i==0):
        l.append(i)
s=0
for j in l:
    s=s+j
print(s==n)
    