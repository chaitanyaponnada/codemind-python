n=input()
s=0
p=1
for i in n:
    i=int(i)
    s=s+i
    p=p*i
print(abs(s-p))