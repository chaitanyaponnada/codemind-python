def pal(n):
    n=str(n)
    if(n==n[::-1]):
        return True
    else:
        return False

n=int(input())
for i in range(n):
    a=input()
    print(pal(a))
        