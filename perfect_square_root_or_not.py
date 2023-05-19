n=int(input())
p=False
for i in range(1,n+1):
    if(i*i==n):
        p=True
        break
print(p)