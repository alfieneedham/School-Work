from sorting_algorithms import bubble_sort, insertion_sort, merge_sort
import random

#tests:
bArrays = [[1,3,7,9,15],
           [1,3,9,7,15],
           [5,4,3,2,1],
           [36,15,28,2,495],
           [],
           ["b","f","c","d","a"],
           [5],
           [0,5,5,7,5,9,5,2],
           [-1,7,0,2,-5]]

iArrays = [[1,3,7,9,15],
           [1,3,9,7,15],
           [5,4,3,2,1],
           [36,15,28,2,495],
           [],
           ["b","f","c","d","a"],
           [5],
           [0,5,5,7,5,9,5,2],
           [-1,7,0,2,-5]]


## testing:
# for array in bArrays:
#     bubble_sort(array)
#     print(array)
# print("")

# for array in iArrays:
#     insertion_sort(array)
#     print(array)
# print("")

def create_array(numNums):
    array = []
    for n in range(numNums):
        array.append(random.randrange(0, 1001))
    return(array)

def test(numNums):
    bArray = []
    iArray = []
    tempArray = create_array(numNums)
    for char in tempArray:
        bArray.append(char)
        iArray.append(char)
    print("Bubble sort took: " + str(round(bubble_sort(bArray),3)) + "s")
    print("Insertion sort took: " + str(round(insertion_sort(iArray),3)) + "s")

test(50000)