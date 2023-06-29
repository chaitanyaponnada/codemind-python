def reverse(n):
    negative=False
    
    if(n<0):
        negative=True
        n=abs(n)
        
    n=str(n)
    n=n[::-1]
    n=int(n)
    if(negative):
        n=n*(-1)
    
    return n
    
n=int(input())
print(reverse(n))