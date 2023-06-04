n=int(input())
b=n*n
b=str(b)
s=[]
for i in b:
    s.append(i)
c=0
for j in s:
    c=c+int(j)
if(c==n):
    print("Neon Number")
else:
    print("Not Neon Number")