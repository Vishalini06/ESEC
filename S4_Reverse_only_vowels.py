a=list(input())
b=[i for i in a if i in "AEIOUaeiou"]
for i in range(len(a)):
   if a[i] in "aeiouAEIOU":
       a[i]=b.pop()
print(''.join(a))       
       
   
   
"""remove only vowels revser and replace
input
hello
itvac
testa
output
holle
atvic
taste"""
