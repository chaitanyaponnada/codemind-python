n=input()
s="aeiouAEIOU"
l=[]
for i in n:
    if(i in s):
        l.append(i)
b=l[::-1]
d=""
c=0
for i in n:
    if(i in l):
        d=d+str(b[c])
        c=c+1
    else:
        d=d+i
print(d)


    