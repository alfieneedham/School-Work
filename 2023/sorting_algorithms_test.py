from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, count_sort
import random
import time

sorts = {"b": bubble_sort, "i": insertion_sort, "m": merge_sort, "c": count_sort}

def time_sort(type, array):
    start = time.time()
    result = sorts[type](array)
    end = time.time()
    delta = round((end - start),3)
    return(delta)

def create_array(numNums):
    array = []
    for n in range(numNums):
        array.append(random.randrange(1, 1001))
    return(array)

def test(numNums):
    #bArray = []
    #iArray = []
    mArray = []
    cArray = []
    tempArray = create_array(numNums)
    for char in tempArray:
        #bArray.append(char)
        #iArray.append(char)
        mArray.append(char)
        cArray.append(char)
    #print("Bubble:", time_sort("b",bArray))
    #print("Insertion:", time_sort("i",iArray))
    print("Merge:", time_sort("m",mArray))
    print("Count:", time_sort("c",cArray))


test(1000000)