a = [12, 15, 16, 19, 22, "f"]

def linear_search(array, value):
    for n in range(len(array)):
        if array[n] == value:
            return(n)
    return(None)

def binary_search(array, value, start_index = 0, end_index = None):
    try:
        int(value)
    except:
        return("Error: value must be an integer.")
    if end_index == None:
        end_index = len(array)
    if start_index >= end_index:
        return(None)
    mid_index = (start_index + end_index) // 2
    try:
        int(array[mid_index])
    except:
        return("Error: all values in array must be integers.")
    if array[mid_index] == value:
        return(mid_index)
    elif array[mid_index] < value:
        return(binary_search(array, value, mid_index + 1, end_index))
    else:
        return(binary_search(array, value, start_index, mid_index))
    

if __name__ == "__main__":
    print(binary_search(a, 1))