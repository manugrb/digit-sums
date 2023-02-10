from matplotlib import pyplot as plt

def main():

    maxLimit = int(input("How many numbers should be calculated with? (In dec)"))
    base = int(input("what base do you want to calculate with?"))

    results = calculateResults(maxLimit, base)
    printResults(results)
    plotResults(results)

def getDigitSum(number, base):

    digitSum = 0

    while number > 0:
        # get the last digit of number and add it to digitSum
        lastDigit = number % base
        digitSum += lastDigit

        # remove the last digit from number before repeating the same process again
        number -= lastDigit
        number = number / base

    return int(digitSum)


def calculateResults(maxLimit, base):

    digitSums = []

    for n in range(maxLimit):
        digitSum = getDigitSum(n, base)
        
        # if the array does not have entries for this digitsum yet set the first entry to 1
        if(digitSum >= len(digitSums)):
            digitSums.insert(digitSum, 1)

        # if the array has entries for this digitsum already, increase it by 1
        else:
            digitSums[digitSum] = digitSums[digitSum] + 1

    return digitSums


def printResults(digitSums):

    # print out the results
    for i in range(len(digitSums)):
        print(str(i) + ' -> ' + str(digitSums[i]))


def plotResults(digitSums):

    plt.bar(range(len(digitSums)), digitSums)
    plt.title('Digit Sums Distribution')
    plt.xlabel('Digit sums')
    plt.ylabel('Occurences')
    plt.show()

if(__name__ == "__main__"):
    main()