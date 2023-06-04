n=int(input())
a=n*n
s=0
for i in str(a):
    i=int(i)
    s=s+i
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")
