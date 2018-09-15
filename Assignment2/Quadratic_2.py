# calculates quadratic and checks for negative discriminates
import math

a = int(input("Given ax^2 + bx + c,\nwhat is the value of a? "))
b = int(input("b? "))
c = int(input("c? "))
d = (b**2) - 4*a*c  # discriminate

if d < 0:  # account for imaginary numbers
    print("There is no real solution")

elif d == 0:  # as to not be repetitive
    x_0 = (-b + math.sqrt((b**2) - (4*a*c))) / (2*a)
    print("There is only one solution, x =", x_0)
else:
    x_n = (-b - math.sqrt((b**2) - (4*a*c))) / (2*a)
    x_p = (-b + math.sqrt((b**2) - (4*a*c))) / (2*a)

    print("Your x values are (", x_n, ",", x_p, ")")
