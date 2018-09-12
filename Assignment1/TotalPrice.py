# program that calculates total cost of item
price = float(input("Enter price of item: "))
rate = float(input("Enter sales tax rate (%): "))

cost = price * ((rate/100) + 1)

print("This item will cost $", cost)
