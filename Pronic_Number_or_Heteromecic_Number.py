def hete(num):
    n = 1
    while n * (n + 1) <= num:
        if n * (n + 1) == num:
            return True
        n += 1
    return False

n=int(input())
if(hete(n)):
    print("YES")
else:
    print("NO")