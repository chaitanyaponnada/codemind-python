n=input().split()
l=[]
for i in n:
    i=list(i)
    l+=i
l=set(l)
l=list(l)
s=["a","e","i","o","u"]
for i in l:
    if(i in s):
        s.remove(i)
print(len(s)==0)
    