def is_abundant_number(n):
    proper_divisors_sum = 0
    
    for i in range(1, n):
        if n % i == 0:
            proper_divisors_sum += i
    
    return proper_divisors_sum > n
n=int(input())
if is_abundant_number(n):
    print(True)
else:
    print(False)
