from array import *
 
p = int(input("enter number of elements: "))

arr = array("i",[])

for i in range(p):
    x = int(input("Enter the value: "))
    arr.append(x)


for e in arr:
    print(e,end=' ')



