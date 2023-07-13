n=input().split()
l=[]
for i in n:
    i=str(i)
    l.append(len(i))
print(min(l))