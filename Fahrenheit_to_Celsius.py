n=int(input())
c=(5/9)*(n-32)
b=round(c,2)
if str(b).endswith("0"):
    print(str(b)+"0")
else:
    print(b)
    