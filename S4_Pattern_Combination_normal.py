n=int(input())

s=65
for i in range(1,n+1):
    print(" "*(n-i)*2,end="  ")
    for j in range(i):
        print(chr(s+j),end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
c=1    
for i in range(n,-1,-1):
    print(" "*(n-i)*2,end="  ")
    for j in range(i):
        print("*",end=" ")
    for k in range(i):
       print(c,end=" ")
       c+=1
    print()   

"""
      A 1
   A B 1 2
A B C 1 2 3
* * * 1 2 3
   * * 4 5 6
      * 7
"""
