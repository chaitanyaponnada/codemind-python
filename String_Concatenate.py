a=input()
b=input()
b=b+a
s=""
for x in sorted(b):
    if(x.isalpha()):
        s=s+str(x)
print(s)