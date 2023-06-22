def is_(number):
    square_root = number ** 0.5
    return square_root == int(square_root)
    
n=int(input())
for i in range(n):
    a=int(input())
    print(is_(a))
    