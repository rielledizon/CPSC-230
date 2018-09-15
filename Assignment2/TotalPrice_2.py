# calculates total price and checks for invalid inputs
price = float(input("What is the price of the object?"))
if price >= 0:
    tax = float(input("What is the sales tax (%) in your state?"))
    if tax > 0:
        total = price * ((tax/100) + 1)
        print("The total price of your item is:", total)
    else:
        print ("That is not a valid value.")
else:
    print ("That is not a valid price.")
