n=int(input())
arr=list(map(int,input().split()))
count = [0, 0]
    
for num in arr:
    count[num] += 1
    
sorted_arr = []
    
for i in range(count[0]):
    sorted_arr.append(0)
    
for i in range(count[1]):
    sorted_arr.append(1)
    
for i in sorted_arr:
    print(i,end=" ")
