n=input()
l=[]
for i in n:
    l.append(int(i))
k=[]
for j in l:
    p=1
    while(j!=0):
        p=p*j
        j=j-1
    k.append(p)
if(int(sum(k))==int(n)):
    print("The number "+str(n)+" is a strong number")
else:
    print("The number "+str(n)+" is not a strong number")
    