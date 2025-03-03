s = eval(input())  # List of strings
k = int(input())  # Exponent value

total = 0  # This will store the final sum

for word in s:
    product = 1  # To store multiplication result for each string
    for char in word:
        product *= ord(char) ** k  # Multiply the exponentiated ordinal values
    
    total += product  # Sum up the product of each string

# Check if the final sum is even or odd
if total % 2 == 0:
    print("EVEN")
else:
    print("ODD")


"""
We have an array of strings. Consider each string as a zero-indexed array of characters. All of the characters will be in the range ascii [a-z] which have decimal values in the range[97-122]. These decimal values are called ordinal values and will be referred toa s ord[a]=97 (for example).

Given an array of strings s=[s[0],s[1],s[2]...,s[n-1]) and an integer m, we calculate a value of each s[i] of length len(s[i]) as:
value[i] = ord[s[i][0]] power m x ord[s[i][1]] power m x ...ord[s[i][len(s-1)] power m.
Perform the calculataion on each string, sum them up and determine whether the sum is ODD or EVEN.

For example, your array s=['abc','abcd'], it has k=2 strings. Rewritten as 2D array of decimal ordinals, we have
s'=[[97,98,99],[97,98,99,100]]. If our exponent is m = 2, we perform the following:

a = 97    9409   
b = 98    9604
c = 99    9801 

s[0] = 'abc' and value of s[0] = 9409 x 9604 x 9801 = 885657916836
s[1] = 'abcd' and value of s[1] = 9409 x 9604 x 9801 x 10000 = 8856579168360000
Adding s[0] and s[1] answer is 8857464826276840
Which is even
If answer is even print EVEN else print ODD

Similarly
['ace','oqs',''oqs'] with m=5 results in an integer 13347265726444778181738809565993
which is ODD

input
['ace','oqs','oqs']
5
result 
ODD 

input
['acf','pqs','oqs']
2
result 
ODD 

input
['dg','pqs']
3
result 
EVEN

input 
['abcdefghijklmnopqrstuvwxyz','pqs','oqs']
12
rrsult 
ODD """
