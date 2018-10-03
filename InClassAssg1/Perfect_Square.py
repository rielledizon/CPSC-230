# says whether number is perfect or not

number = int(input("Please enter a number to check:"))
# find and sum up the divisors
divisor = 1
sumdivisors = 0
while divisor < number:
    if number % divisor == 0:
        sumdivisors = sumdivisors + divisor
        divisor = divisor + 1
# classify the result
if number == sumdivisors:
    print(number, "is perfect")
else:
    print(number, "is not perfect")
