from array import *    
def printRepeating(arr, size):
 
    print("Repeating elements are ",
                         end = '')
    for i in range (0, size-1):
        for j in range (i + 1, size):
            if arr[i] == arr[j]:
                print(arr[i], end = ' ')
 
 
# Driver code
arr = []
z = int(input())


for j in range(0,z):
    lst = int(input())
    arr.append(lst)

size = len(arr)
printRepeating(arr, size)

