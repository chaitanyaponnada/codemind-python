m=int(input())
n=int(input())
l=[]
d=[]
for i in range(1,m):
    if(m%i==0):
        l.append(i)
for i in range(1,n):
    if(n%i==0):
        d.append(i)
if(sum(l)==n) and(sum(d)==m):
    print("Amicable")
else:
    print("Not Amicable")
        