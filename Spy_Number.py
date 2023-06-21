n=input()
s=0
p=1
for i in n:
    i=int(i)
    s=s+i
    p=p*i
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")
    