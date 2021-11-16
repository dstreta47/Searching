
def binarysearch(array,target):
    L = 0
    R = len(array)-1
    while(L<=R):
        mid = (L+R)//2
        if array[mid] == target:
            return array[mid]
        elif target > array[mid]:
            L = mid +1 
        else:
            R = mid -1      

    return -1          



array = [0,1,21,33,45,45,61,71,72,73]
target = 33
print(binarysearch(array,target))
