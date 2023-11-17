values = [2, 3, 5, 7, 11, 13]

# doubles each of values.
doubles = [n*2 for n in values]

# if ends in 3, set to 0.
anotherList = [(n if n%10!=3 else 0) for n in values]

#does same as above thing.
def f(x):
    if x%10 == 3:
        return 0
    else:
        return x
yetAnotherList = [f(x) for x in values]
#alternative syntax:
yetAgainAnotherList = list(map(f, values))

print(doubles)
print(anotherList)
print(yetAnotherList)
print(yetAgainAnotherList)