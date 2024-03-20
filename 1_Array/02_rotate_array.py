from array import *

def rotate_array(arr , k):
    for i in range(k):
        temp = arr.pop()
        arr.insert(0,temp)
    return arr

if __name__=='__main__':
    arr = array('b',[])
    n = int(input())
    for i in range(n):
        m = int(input())
        arr.append(m)
    k=int(input())
    new_arr = rotate_array(arr,k)
    for x in new_arr:
        print(x,end=' ')
    
