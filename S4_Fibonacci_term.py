n = int(input())  # Read input N
a, b = 0, 1       # Start with F(0) = 0, F(1) = 1

for _ in range(n - 1):  # Loop from 2 to N
    a, b = b, (a + b) % 100  # Only keep last 2 digits

print(b if b > 9 else b)  # Ensure no leading zero

""'
 Given a number N. Find the last two digits of the Nth fibonacci number.

Fibonacci starts with 0,1,1
0 is the 0th term, 1 is the first term, 1 is the second term
So Fib(2) = 1

Note: If the last two digits are 02, return 2.

Example 1:

Input:
N = 13
Output:
33
Explanation:
The 13th Fibonacci number is 233.
So last two digits are 3 and 3.
 input
12
output 44"""
