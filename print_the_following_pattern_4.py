n=int(input())

for i in range(n):
    i=i+1
    s=""
    for j in range(n):
        if(j==(i-1) or j==(n-i)):
            s=s+"x"
        else:
            s=s+"0"
    print(s)
