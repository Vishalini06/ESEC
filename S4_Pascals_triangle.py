n=int(input())
r=[[1]*(i+1) for i in range(n)]
print("** Printing the pattern... **")
for i in range(2,n):
    for j in range(1,i):
        r[i][j]=r[i-1][j-1]+r[i-1][j]
for i in range(n):
    if n==3:
        print(" "*(n-i-1),end="")
        print(" ".join(map(str,r[i])))
    else:
        print(" "*(n-i-1),end="")
        print(" ".join(map(str,r[i])))
