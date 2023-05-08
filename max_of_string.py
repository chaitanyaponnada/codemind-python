n=input()
c=[]
a="abcdefghijklmnopqrstuvwxyz"
for i in range(len(a)):
    for j in range(len(n)):
        if(n[j]==a[i]):
            c.append(i)
x=max(c)
print(a[x])
            
    
