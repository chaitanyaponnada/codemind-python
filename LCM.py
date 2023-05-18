a=list(map(int,input().split()))
if(a[0]>a[1]):
    s=a[0]
else:
    s=a[1]
lcm=s

gotlcm=False

for i in range(s,a[0]*a[1]+1):
    if not(gotlcm):
        if(i%a[0]==0 and i%a[1]==0):
            gotlcm=True
            lcm=i
print(lcm)