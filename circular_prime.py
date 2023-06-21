def prime(n):
    if(n==1):
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
                break
    return True

n=int(input())
s=prime(n)
n=str(n)
n=n[::-1]
n=int(n)
k=prime(n)
if(s==True and k==True):
    print("circular prime")
elif(s==True):
    print("prime but not a circular prime")
else:
    print("not prime")