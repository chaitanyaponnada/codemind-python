def calculate_handshakes(n):
    if n < 2:
        return 0
    
    handshakes = (n * (n - 1)) // 2
    
    return handshakes

num_people = int(input())
max_handshakes = calculate_handshakes(num_people)
print(max_handshakes)
