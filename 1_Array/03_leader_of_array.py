'''
Find the leaders in an array: An element in an array is considered a leader if it is greater than all the elements to its 
right side. Write a function that takes an array and returns a list containing only the leaders.
'''

from array import *

def leader_array(n,arr):
    leader=[]
    max=arr[n-1]
    leader.insert(0,max)
    for i in range(n-2,-1,-1):
        temp=arr[i]
        print(temp)
        if(temp>max):
            max=temp
            leader.insert(0,max)

    return leader

if __name__=="__main__":
    n=int(input("Enter a number of elements in array : "))
    arr = array('b',[])
    for i in range(n):
        m=int(input())
        arr.append(m)
    ans = leader_array(n,arr)
    print("Leader of array : ",ans)

    