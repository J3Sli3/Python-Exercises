print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
cost = 0

if size == "S":
    cost += 15
elif size == "M":
    cost += 20
elif size == "L":
    cost += 25
else:
    print("You typed the wrong inputs.")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y" and size == ("S"):
    cost += 2
elif pepperoni == "Y" and size == ("M" or "L"):
    cost += 3
elif pepperoni == "N":
    cost += 0
else:
    print("You typed the wrong inputs.")

cheese = input("Do you want extra cheese? Y or N: ")
if cheese == "Y":
    cost += 1
elif cheese == "N":
    cost += 0

print(f"Your final bill is: ${cost}.")


