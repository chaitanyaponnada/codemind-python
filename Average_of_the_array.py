n=int(input())
a=map(int,input().split())
s=0
for i in a:
    s=s+int(i)
z=float(s/n)

r=round(z,2)

print(str(r)+"0")