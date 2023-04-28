import time
from math import inf

a = [5,4,3,2,1,0]
b = [3465,568,345,568,4,457,6799,35]
c = [1,2,4,6,8,9,19]
d = [1,3,4,6,8,11,15]

# The inputted array is sorted.
def bubble_sort(array):
    start = time.time()
    for passes in range(len(array)):
        madeSwap = False
        for comparisons in range(len(array)-passes-1):
            if array[comparisons] > array[comparisons+1]:
                madeSwap = True
                array[comparisons], array[comparisons+1] = array[comparisons+1], array[comparisons]
        if madeSwap == False:
            break
    end = time.time()
    delta = end - start
    return(delta)

# The inputted array is sorted.
def insertion_sort(array):
    start = time.time()
    for passes in range(len(array)-1):
        index = passes
        while index != -1:
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                index -= 1
            else:
                break
    end = time.time()
    delta = end - start
    return(delta)

# Returns the sorted array. Original array remains unchanged.
def merge(arrayOne, arrayTwo):
    arrayOne.append(inf)
    arrayTwo.append(inf)
    result = []
    pointerOne = pointerTwo = 0
    while pointerOne < len(arrayOne)-1 or pointerTwo < len(arrayTwo)-1:
        if arrayOne[pointerOne] <= arrayTwo[pointerTwo]:
            result.append(arrayOne[pointerOne])
            pointerOne += 1
        else:
            result.append(arrayTwo[pointerTwo])
            pointerTwo += 1
    return(result)
def merge_sort(array):
    if len(array) <= 1:
        return(array)
    leftHalf = merge_sort(array[:len(array)//2])
    rightHalf = merge_sort(array[len(array)//2:])
    return(merge(leftHalf, rightHalf))

if __name__ == "__main__":
    print(b)
    b=merge_sort(b)
    print(b)
    print(merge_sort(b))