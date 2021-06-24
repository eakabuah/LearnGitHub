from array import *

vals = array('i', [5,9,8,4,2])

newArr = array(vals.typecode, (a*a for a in vals))

for i in newArr:
    print(i)

print("Familiarizing with git")
print("Another change to test familiarity")
print("One more line")