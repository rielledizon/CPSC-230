# calculate standard deviation and mean of given values

# import module for use of square root
import math

# variable for list of numbers
num_list = []

# sets while loop to keep going until negative value is given
loop = True

print("Enter one value at a time then enter a negative value when "
      "you are ready\nto get the mean and standar deviation of all "
      "values.")
print ()

# begin while loop to get a list of numbers
while loop:
    number = float(input("Enter a value: "))
    print ()
    if number >= 0:
        # method to add each number given
        num_list.append(number)
    else:
        break

# method to sort
num_list.sort()

print ('The numbers you inputed are: ', num_list)
print ()

# equation for mean/average of all numbers
mean = sum(num_list) / len(num_list)
print ('The mean of all values is: ', mean)
print()

# variable for variance to prepare for a summmation of all numbers
var = 0

# for loop to calculate variance
for x in num_list:

    # equation for variance
    summation = (x - mean)**2
    var += summation

# equation for standard deviation
stan_dev = math.sqrt(var / len(num_list))

print ('The standard deviation of all values is: ', stan_dev)
print ()
