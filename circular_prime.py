def prime(n):
    n=int(n)
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
    
n=int(input())
z=str(n)
z=z[::-1]
if(prime(n) and prime(z)):
    print("circular prime")
elif(prime(n) and prime(z)==False):
    print("prime but not a circular prime")
else:
    print("not prime")
