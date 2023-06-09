n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    z=i*i
    l.append(z)
s=""
for i in sorted(l):
   print(i,end=" ")