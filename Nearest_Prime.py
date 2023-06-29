
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def near(num):
    if prime(num):
        return num
    i=d=num
    while True:
        i-= 1
        d+= 1

        if prime(i):
            return i
        if prime(d):
            return d

    
n=int(input())
for i in range(n):
    a=int(input())
    print(near(a))