import math

maxLimit = int(input("How many numbers should be calculated with? (In dec)"))
base = 10

def getDigitSum(number):

    digitSum = 0

    while number > 0:
        # get the last digit of number and add it to digitSum
        lastDigit = number % 10
        digitSum += lastDigit

        # remove the last digit from number before repeating the same process again
        number -= lastDigit
        number = number / 10

    return int(digitSum)

digitSums = []

for n in range(maxLimit):
    digitSum = getDigitSum(n)
    
    if(digitSum >= len(digitSums)):
        digitSums.insert(digitSum, 1)
    else:
        digitSums[digitSum] = digitSums[digitSum] + 1

for i in range(len(digitSums)):
    print(str(i) + ' -> ' + str(digitSums[i]))