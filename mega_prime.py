def prime(n):
    if(n==1):
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
                break
    return True

n=input()
a=prime(int(n[0]))
b=prime(int(n[1]))
c=prime(int(n))
if( a==b and b==c and c==a):
    print("Mega Prime")
else:
    print("Not Mega Prime")
