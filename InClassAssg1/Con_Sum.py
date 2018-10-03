# code that calculates that asks user for
# a number and adds each natural number consecutively

numElements = int(input("Enter a number? "))

# intialize loopCounter and totalSum
loopCounter = 0
totalSum = 0

# while loop that stops when number of inputs is reached
while loopCounter < numElements:
    loopCounter += 1
    totalSum += loopCounter
print ("Your total sum of consecutive numbers is:", totalSum)
