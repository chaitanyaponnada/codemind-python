n=input().split()

c=0
for i in n:
    for j in i:
        if(j.islower()):
            c=c+1
print(c)