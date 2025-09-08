print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")



price = 0

if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L":
    price += 25
else:
    print("Error. Please enter a valid size")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3
    
elif pepperoni != "N":
    print("Error. Please enter \"Y\" or \"N\"")

extra_cheese = input("Do you want extra cheese? Y or N: ")

if extra_cheese == "Y":
    price += 1
elif extra_cheese != "N":
    print("Error. Please enter \"Y\" or \"N\"")
    
print(f"The price of your pizza is £{price}")
