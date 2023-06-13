n=input()
l=[]
d=[]
for i in range(65,91):
    l.append(chr(i))
for j in range(97,123):
    d.append(chr(j))
z=l+d
c=0
m=0
for i in n:
    if(str(i) in str(z)):
        m=m+1
    else:
        c=c+1
print(c)