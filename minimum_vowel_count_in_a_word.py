n=input().split()
s="AEIOUaeiou"
l=[]
for i in n:
    c=0
    for j in i:
        if j in s:
            c=c+1
    l.append(c)
print(min(l))