n=input()
z=len(n)
s=0
for i in range(z):
    a=n[i]
    a=int(a)
    b=int(i+1)
    x=a**b
    s=s+int(x)
print(str(s)==str(n))
    