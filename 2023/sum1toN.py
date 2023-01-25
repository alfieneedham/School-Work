num = int(input("Enter num: "))

totalLoop = 0
totalEquation = 0

if num >= 1:
    
    totalEquation = (num/2)*(num+1)
    print("By equation:", str(totalEquation))
    
    for i in range(1, num+1):
        totalLoop += i
    print("By loop: ", str(totalLoop))

else:
    print("Num must be >= 1")