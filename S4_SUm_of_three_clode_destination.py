from itertools import combinations
n,tar=list(map(int,input().split()))
arr=list(map(int,input().split()))

c=combinations(arr,3)
a=set()
for i in c:
    a.add(sum(i))
for i in a:
   if i==tar:
      print(i)

"""
Given an array of T integers and another integer destination, find three integers in the array such that the addition is closest to destination. Your task is to identify the addition of the three integers.

Note:

If they exist over one answer, then display maximum sum

Input Format

The first line of input contains T and target. Next line contains Array elements

Output Format

Display sum of three integers

Sample input:

6 2
-7 9 8 3 1 1
Output:
2

Explanation
-7+8+1= 2 
which is the closest to the expected input. So this is the output

For example:

Input	Result
6 2
-7 9 8 3 1 1
2
4 13
5 2 7 6
13
"""
