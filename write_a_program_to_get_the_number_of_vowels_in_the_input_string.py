n=input()
s="aeiouAEIOU"
c=0
for i in n:
    for j in s:
        if(i==j):
            c=c+1
print(c)
    