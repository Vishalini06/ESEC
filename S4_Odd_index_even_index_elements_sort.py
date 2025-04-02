n = int(input())
arr = list(map(int, input().split()))

odd=sorted([arr[i] for i in range(0,n,2)],reverse=True)
even=sorted([arr[i] for i in range(1,n,2)])

od=0
ev=0

for i in range(n):
    if i%2==0:
       arr[i]=odd[od]
       od+=1
    else:
       arr[i]=even[ev]
       ev+=1
print(*arr)       


"""odd index in desending and even index elements in ascending
input
10
123456789 10
output
9 2 7 4 5 6 3 8 1 10"""
