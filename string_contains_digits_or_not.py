n=int(input())
for i in range(n):
    a=input()
    z=False
    l=[]
    for j in a:
        if(j.isdigit()):
            z=True
    if(z):
        print("Yes")
    else:
        print("No")