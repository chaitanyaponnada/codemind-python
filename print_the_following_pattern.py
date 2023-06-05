n=int(input())
for i in range(1,n+1):
    s=""
    for j in range(1,n+1):
        if i==j:
            s=s+"0"
        else:
            s=s+"x"
    print(s)
            