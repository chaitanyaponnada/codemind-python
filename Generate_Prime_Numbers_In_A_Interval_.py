def prime(n):
    if(n==1):
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
                break
    return True

m=int(input())
n=int(input())
for i in range(m,n):
    if(prime(i)):
        print(i)