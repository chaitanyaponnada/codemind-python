n=input()
a=input()
a=a.replace(" ","")
c=True
for i in a:
    if(i=="0" or i=="1"):
        c=True
    else:
        c=False
        break
print(c)
        