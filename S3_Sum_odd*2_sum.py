
"""arr=list(map(int,input()))
add=0
for i in range(len(arr)):
   if i%2==0:
      a=arr[i]*2
      if a>9:
         s=0
         for i in str(a):
            s+=int(i)
         add+=s
      else:
        add+=a
   else:
      add+=arr[i]
print(add)      

"""
For a given integer n, take each digit from left to right. If the number is in odd place then multiply by 2. If the result is greater than 10, add the digits to find the total and add to sum. If it is even digit directly add to sum. Print the sum

Example 83641

8,6,1 are in odd place and 3,4 are in even place
First we take 8, multiply by 2 which is 16. Add the digits 1+6 = 7, SUM = 7
3 is in even place, so we just add to 7, SUM = 10
Next we take 6, multiply by 2 which is 12. Add the digits 1+2 = 3, SUM = 13
4 is in even place, so we add it to 13, SUM = 17
Next we take 1 which is odd place. We multiply by 2. Since the result is less than 10, we directly add it to SUm = 19
So answer is 19

For example:

Input	Result
83641
19
111111
9
"""
            
