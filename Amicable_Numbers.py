m=int(input())
n=int(input())
l=[]
d=[]
for i in range(1,m):
    if(m%i==0):
        l.append(i)
for j in range(1,n):
    if(n%j==0):
        d.append(j)
x=sum(l)
y=sum(d)
if(int(n)==int(x)) and (int(m)==int(y)):
    print("Amicable")
else:
    print("Not Amicable")
# print(x,n,y,m)