n=input().split()
l=[]
for i in n:
    for j in i:
        j=j.lower()
        l.append(j)
a=(sorted(set(l)))

x=97
y=123
z=[]
for i in range(x,y):
    z.append(chr(i))
    
print(a==z)