n=int(input())
a=list(map(int,input().split()))
z=a[::-1]
if(z==sorted(a)):
    print("yes")
else:
    print("no")
