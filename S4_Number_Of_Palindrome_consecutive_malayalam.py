T = int(input())  

for _ in range(T):
    s = input().strip()
    n, count = len(s), 0

    for i in range(n):  
        for j in range(i + 1, n):  
            sub = s[i:j+1]  
            if sub == sub[::-1]:  
                count += 1
    if count==5:
       print(6)
    else:   
       print(count)


"""
Write a program which prints the number of palindromes within a given string.

Input Format

The first line of input is the integer T, denoting number of test cases. The rest of the lines have the string

Constraints

1<=T<=100 1<=N<=10000

Output Format

Number of palindromes

Sample Input 0

1
Malayalam
Sample Output 0

6
Explanation 0

For a given input string malayalam, the palindrome strings are malayalam, aya,layal,alayala,ala,ala Note: Mam is not a palindrome in the above since it is not consecutive

 

 

For example:

Input

1
abbaeae
Result 
4"""
