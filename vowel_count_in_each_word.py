n=input().split()
s="AEIOUaeiou"
for i in n:
    c=0
    for j in i:
        if j in s:
            c=c+1
    print(c,end=" ")