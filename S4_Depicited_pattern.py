a=int(input())
n=2*a-1
for i in range(n):
    for j in range(n):
        print(a-min(i,j,n-i-1,n-j-1),end=" ")
    print()    
