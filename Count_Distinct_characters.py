n=input().split()
l=[]
for i in n:
    i=str(i)
    l+=list(i.lower())
print(len(set(l)))