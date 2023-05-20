n=input()
c=0
res=0
for i in n:
    c+=1
    res=res+int(i)**c

print(res==int(n))
    
    