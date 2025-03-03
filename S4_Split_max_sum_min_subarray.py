t = int(input())  
for _ in range(t):
    n, k = map(int, input().split())  
    arr = list(map(int, input().split()))  

    l, r = max(arr), sum(arr)  

    while l < r:
        m = (l + r) // 2
        subarrays, s = 1, 0

        for num in arr:
            if s + num > m:
                subarrays += 1
                s = num
            else:
                s += num

        if subarrays <= k:
            r = m  
        else:
            l = m + 1  

    print(l)

"""
Split the given array into K sub-arrays such that maximum sum of all sub arrays is minimum

Given an Array[] of N elements and a number K. ( 1 <= K <= N ) . Split the given array into K subarrays (they must cover all the elements). The maximum subarray sum achievable out of K subarrays formed, must be minimum possible. Find that possible subarray sum.

Input format:  First line number of test cases

Second line Two space separated integers N and K.and followed by elements of array.

Constraints:

1≤T≤100

1≤K≤N≤104

1≤Ai ≤105

Sample Input

1

5 3

1 2 3 4 5

Sample output:

6

Explanation: Optimal Split is {1, 2, 3}, {4}, {5}. Maximum sum of all subarrays is 6, which is minimum possible for 3 splits."""
