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

    return digitSum
