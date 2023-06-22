n=int(input())

while(n>=9):
    n=str(n)
    s=0
    for i in n:
        s=s+int(i)
    n=s
print(n)