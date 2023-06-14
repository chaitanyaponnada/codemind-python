n=input()
o=0
e=0
for i in n:
    i=int(i)
    if(i%2==0):
        e=e+1
    else:
        o=o+1
if(e!=0 and o!=0):
    print("Mixed")
elif(e!=0):
    print("Even")
else:
    print("Odd")
    