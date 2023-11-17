tl1 = [1,2,3,4,5,6,7,8,9]
tl2 = [2,4,6,8,10,12,14,16,18]
tl3 = [3,8,5,19,94,2,7,56,53]
tl4 = ["a", "B", "c", "d", "D", "E", "F", "f", "g"]
tl5 = ["abCDe", "aABbC", "aaAAAbBbbCCdddDEefG", "fjAHFgjfiGIRdkavjgjDIG", "abcdefg"]

# Map Excercises:
def mapEx1(l):
    return (list(map(lambda n: n*3, l)))

def mapEx2(l1, l2, l3):
    l = list(zip(l1, l2, l3))
    return (list(map(lambda n: n[0]+n[1]+n[2], l)))

def mapEx3(l):
    return(list(map(lambda n: n**2, l)))

def mapEx4(l):
    l = list(map(lambda n: n.upper(), l))

    def remDupes(s):
        occurences = []
        s = list(s)
        for char in s:
            if char in occurences:
                s.remove(char)
            else:
                occurences.append(char)
        return(s)
    
    return(list(map(remDupes, l)))






# Filter Excercises:
def filEx1(l):
    return (list(filter(lambda n: n%2==0, l)))

def filEx2(l):
    return (list(filter(lambda c: c.isupper(), l)))

def filEx3(l, max):
    return (list(filter(lambda n: n<=max, l)))



# print(mapEx1(tl1))
# print(redEx1(tl1))
# print(mapEx2(tl1,tl2,tl3))
# print(filEx2(tl4))
# print(mapEx3(tl1))
# print(filEx3(tl3, 53))
print (mapEx4(tl5))