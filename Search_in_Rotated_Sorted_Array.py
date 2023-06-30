n=int(input())
a=list(map(int,input().split()))
s=int(input())
for i in range(len(a)):
    if(a[i]==s):
        print(i)
        break
else:
    print(-1)