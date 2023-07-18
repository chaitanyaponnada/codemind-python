def pos(n,s):
    n=str(n)
    for i in n:
        if(i==s):
            a=n.index(i)
            return a
            break
    else:
        return 0
        
n=input()
s=input()
z=pos(n,s)
if(z==0):
    print(False)
else:
    print(True)
    print(z)