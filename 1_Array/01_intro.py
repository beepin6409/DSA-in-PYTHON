from array import *

arr = array('b',[2,3,4,5])
for x in arr:
    print(x,end=' ')

print("\n")

for i in range(4):
    print(arr[i],end=' ')

arr.append(23)
arr.insert(2,45)    # inserting 45 at 2nd index or 3rd position

arr.count(2)        # count occurence of 2 in array

print("Pop : ",arr.pop())   #if index passed in pop , it will delete in that index . Default : Last position

arr.remove(4)                 # remove 4 from array






            