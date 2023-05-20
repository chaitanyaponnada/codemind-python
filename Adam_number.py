n=int(input())

a=n*n

n=str(n)

nr=n[::-1]

nr=int(nr)

b=nr*nr
a=str(a)
b=str(b)

print(a[::-1]==b)