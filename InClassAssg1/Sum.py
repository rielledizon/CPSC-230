# code that calculates that asks user for
# amount of inputs and adds each input Given

numElements = int(input("How many numbers would you like to sum? "))

# intialize loopCounter and totalSum
loopCounter = 0
totalSum = 0

# while loop that stops when number of inputs is reached
while loopCounter < numElements:
    numGiven = int(input("Enter a number: "))
    totalSum += numGiven
    loopCounter += 1
print ("Your total sum is:", totalSum)
