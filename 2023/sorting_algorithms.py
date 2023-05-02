import time
from math import inf

array = ["3456", "1234", "2367", "2345", "6789", "4567", "5467"]

# The inputted array is sorted.
def bubble_sort(array):
    for passes in range(len(array)):
        madeSwap = False
        for comparisons in range(len(array)-passes-1):
            if array[comparisons] > array[comparisons+1]:
                madeSwap = True
                array[comparisons], array[comparisons+1] = array[comparisons+1], array[comparisons]
        if madeSwap == False:
            break

# The inputted array is sorted.
def insertion_sort(array):
    for passes in range(len(array)-1):
        index = passes
        while index != -1:
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                index -= 1
            else:
                break

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

def count_sort(array):
    largestNum = None
    for value in array:
        if largestNum == None or value > largestNum:
            largestNum = value
    tally = [0]*(largestNum+1)
    result = [0]*len(array)
    for value in array:
        tally[value] += 1
    for i in range(1,len(tally)):
        tally[i] += tally[i-1]
    for value in array:
        result[tally[value-1]] = value
        tally[value-1] += 1
    return(result)  

if __name__ == "__main__":
    pass