num = int(input("Enter num: "))

totalLoop = 0
totalEquation = 0

if num >= 1:
    for i in range(1, num+1):
        totalLoop += i
    print("By loop: ", str(totalLoop))

    totalEquation = (num/2)*(num+1)
    print("By equation:", str(totalEquation))

else:
    print("Num must be >= 1")