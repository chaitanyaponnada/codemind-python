a="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
n=int(input())

for i in range(0,n):
    s=""
    for j in range(1,n+1):
        s=s+str(a[2*i])+" "
    print(s)
    
        
        