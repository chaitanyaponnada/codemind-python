n=input()
c=0
for i in n:
    if i.isdigit():
        c=c+1
if c>0:
    print("Contains "+str(c)+" digit")
else:
    print("Doesn't contain digit")
    
        
