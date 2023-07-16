n=list(input())
s=set(n)
s=list(s)
if(sorted(n)==sorted(s)):
    print("Unique Number")
else:
    print("Not Unique Number")