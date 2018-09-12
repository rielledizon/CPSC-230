# calculates quadratic only for positive discriminates
import math

a = float(input("Given ax^2 + bx + c,\nWhat is the value of a? "))
# \n for line break in shell
b = float(input("b? "))
c = float(input("c? "))

x_n = (-b - math.sqrt((b**2)-(4*a*c))) / (2*a)
x_p = (-b + math.sqrt((b**2)-(4*a*c))) / (2*a)
# negative and positive roots
print("x1:", x_n, "and x2:", x_p,)
