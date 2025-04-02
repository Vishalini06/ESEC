"""Write a program to find the number of ways in which you can add up to a number

For input 5

Input:
5

Output:
7

Explanation:
[1, 1, 1, 1, 1, ]

[1, 1, 1, 2, ]

[1, 1, 3, ]

[1, 2, 2, ]

[1, 4, ]

[2, 3, ]

[5,]

For input 

4

Output:

5

Explanation:

[1, 1, 1, 1, ]

[1, 1, 2, ]

[1, 3, ]

[2, 2, ]

[4,]



For example:

Input	Result
4
5
5
7
30
5604
82
20506255"""

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1  # Base case

for num in range(1, n + 1):  # Consider numbers 1 to n
    for j in range(num, n + 1):  # Update ways to sum up to j
        dp[j] += dp[j - num]

print(dp[n])  # Final answer



