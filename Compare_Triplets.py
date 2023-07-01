def ans(a,x):
    s1=0
    s2=0
    for i in range(3):
        if(a[i]>x[i]):
            s1=s1+1
        elif(a[i]<x[i]):
            s2=s2+1
        else:
            pass
    return(s1,s2)



a=list(map(int,input().split()))
x=list(map(int,input().split()))
r1,r2=ans(a,x)
print(r1,r2)