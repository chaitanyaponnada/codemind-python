def prime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
            break
    return True
    
def pal(m):
    m=str(m)
    return m==m[::-1]
    
a=int(input())
a=a+1
while(True):
    if(prime(a)==True and pal(a)==True):
        print(a)
        break
    else:
        a=a+1