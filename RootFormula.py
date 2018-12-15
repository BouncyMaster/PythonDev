import math

print("Please type in your coefficients: ")
firstCoeff = int(input("First coefficient: "))
secondCoeff = int(input("Second coefficient: "))
thirdCoeff = int(input("Third coefficient: "))
print("a: %d b: %d c: %d" % (firstCoeff, secondCoeff, thirdCoeff))

root = math.sqrt((secondCoeff**2) - (4 * firstCoeff * thirdCoeff))
x1 = (-secondCoeff + root) / (2 * firstCoeff)
x2 = (-secondCoeff - root) / (2 * firstCoeff)


if x1 != x2:
    print("The answers are: (x1, x2) (%.2f , %.2f)" % (x1, x2))
elif x1 == x2:
    print("The answer is: x = %.2f" % x1)
else:
    print("Something went wrong. Please try again.\n")
mainLoop = input("Press the Enter key to close this window.")
