def prime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
            break
    return True
    
def nop(m,n):
    p=[]
    for i in range(m,n+1):
        if prime(i):
            p.append(i)
    return p

   
a=int(input())
b=int(input())

print(len(nop(a,b)))