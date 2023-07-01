def pal(a):
    a=str(a)
    return(a==(a[::-1]))

n=int(input())
for i in range(n):
    a=input()
    s=""
    if(pal(a) and len(a)%2==0):
        print("YES EVEN")
    elif(pal(a) and len(a)%2!=0):
        print("YES ODD")
    else:
        print("NO")
        