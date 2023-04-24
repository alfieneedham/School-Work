from search_algorithms import binary_search, linear_search

def search(array, value):
    return(linear_search(array, value), binary_search(array, value))

a = [0, 1, 13, 27, 49, 456]
b = [0, 2, 5, 7]
c = ["a", 456, "search"]
d = [-12, -7, 5, 9]

print(search(a,13))
print(search(a,0))
print(search(a,456))
print(search(a,87))
print(search(b,0))
print(search(b,2))
print(search(b,5))
print(search(b,7))
print(search(b,8))
print(search(c, "a"))
print(search(c, 456))
print(search(c, "search"))
print(search(c, "car"))
print(search(c, 559))
print(search(d, -12))
print(search(d, -7))
print(search(d, 5))
print(search(d, 9))
print(search(d, 10))
print(search(d, -13))