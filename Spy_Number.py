n=input()
a=[]
for i in n:
    if i.isdigit():
        a.append(i)
k=0
s=1
for j in a:
    s=s*int(j)
    k=k+int(j)
if(s==k):
    print("Spy Number")
else:
    print("Not Spy Number")
    
