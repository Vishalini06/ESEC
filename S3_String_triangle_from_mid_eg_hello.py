s="PROGRAM"
m=len(s)//2
n=s[m:]+s[:m]
for i in range(1,len(s)+1):
    for j in range(i):
        print(n[j],end="")
    print()    

print()

"""output
G
GR
GRA
GRAM
GRAMP
GRAMPR
GRAMPRO

input
hello
output
l
ll
llo
lloh
llohe"""
