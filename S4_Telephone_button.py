from itertools import product
n=input()
arr=[" ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
if n=="1":
    print("No Combination of Strings")

else:
    num=[]
    for i in n:
       num.append(arr[int(i)-1])
    com=["".join(p) for p in product(*num)]
    print(*com) 
          
       
    
    
