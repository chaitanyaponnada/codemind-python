a=input()
numbers =list(map(int,input().split()))
most_frequent_num = max(set(numbers), key=numbers.count)
print(most_frequent_num)
