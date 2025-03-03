s = input().split(';')

ints, chars = {}, {}

for stmt in s:
    if stmt.strip():
        d = ints if "int" in stmt else chars
        for v in stmt.split(' ', 1)[1].split(','):
            k, v = (v.split('=') + ["junk"])[:2]
            d[k.strip()] = v.strip()

print("Integers")
print("\n".join(f"{k}={v}" for k, v in ints.items()))
print("Characters")
print("\n".join(f"{k}={v}" for k, v in chars.items()))

""" Given a C style initialization statement find the variable types and values. Only int and char are allowed. If a variable is not initialized it should be marked as “junk”.

Sample Input 1
int b,a=10;char s='a';
Sample Output 1
Integers
b=junk
a=10
Characters
s='a'
Sample Input 2
int i,k=10;int a=-10;char b='c';
Sample Output 2
Integers
i=junk
k=10
a=-10
Characters
b='c'"""
