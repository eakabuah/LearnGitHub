from array import *

vals = array('i', [5,9,8,4,2])

newArr = array(vals.typecode, (a*a for a in vals))
newArr2 = array(vals.typecode, (a*a*a for a in vals))
for i in newArr:
    print(i)

for i in newArr2:
    print(i)

print("Additional Changes.")
