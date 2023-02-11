from matplotlib import pyplot as plt


def main():

    maxLimit = int(input("How many numbers should be calculated with? (In dec)"))
    base = int(input("what base do you want to calculate with?"))
    dampingPower = int(input("what power do you want the damping interval to have?"))
    dampingCoefficient = base ** dampingPower
    result = calculateResults(maxLimit=maxLimit, base=base, dampingCoefficient=dampingCoefficient)
    
    plotResults(result=result)


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

def calculateResults(maxLimit, base, dampingCoefficient):

    result = []

    for n in range(int(maxLimit / dampingCoefficient)):
        totalDigitSum = 0
        currentNumber = n * dampingCoefficient

        for d in range(dampingCoefficient):
            totalDigitSum += getDigitSum(currentNumber + d, base)

        averageDigitSum = totalDigitSum / dampingCoefficient
        result.append(averageDigitSum)

    return result


def plotResults(result):

    plt.plot(result)
    plt.title('Digit Sum Distribution')
    plt.xlabel('n of damping intervals')
    plt.ylabel('Digit sums')
    plt.show()

if(__name__ == "__main__"):
    main()