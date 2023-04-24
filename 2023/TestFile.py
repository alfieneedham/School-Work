nums = ("4163636f756e74204e756d6265723a2037323434303937333531")
numlist = []
temp = ""

for char in nums:
    temp += char
    if len(temp) == 4:
        numlist.append(temp)
        temp = ""

print(numlist)

#16739 25455 30062 29728 20085