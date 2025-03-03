for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    l, r, turn, max_val, unique_value = 0, n - 1, 1, max(arr), 0

    while l <= r:
        if arr[l] < arr[r]:  
            unique_value += arr[l] * turn + max_val
            l += 1
        else:
            unique_value += arr[r] * turn + max_val
            r -= 1
        
        turn += 1
        max_val = max(arr[l:r+1]) if l <= r else 0  # Update max in remaining array

    print(unique_value)

""" Unique element problems

You are given an array Array of size N.

Perform the following operations to delete the array so that you can maximize the value of a unique array element:

For any turn i(1≤ i≤ N),delete either of the end elements.

Before deleting the array element at index K, it contributes the value arr[K]*turni+SVi to the unique value where turni is the number of the turn in which you are performing the operation

SVi is a sustaining value that is the value of the maximum element present in the array before the ithturn is made

Write a program to print the maximum unique value that can be obtained after the array ids completely deleted

INPUT FORMAT:

The first line:T denoting the number of test cases, followed by size of array and elements of array

Constraints:

1 ≤ T ≤ 10

1≤ N ≤ 103

1 ≤Arri≤ 106

Explanation:

INPUT:

1

5

5 4 3 6 2

OUTPUT:

96

The order we follow to detroy the given array is:

2*1+6=8

5*2+6=16

4*3+6=18

3*4+6=18

6*5+6=36

Now 8+16+18+18+36=96

 

 

For example:

Input	
1
5
5 4 3 6 2
Result
96"""
