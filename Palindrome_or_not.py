def pal(a):
    a=a.lower()
    z=a[::-1]
    return z==a
n=input()
print(pal(n))