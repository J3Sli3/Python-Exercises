print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
cost = 0

if size == "S" or size == 's':
    cost += 15
elif size == "M" or size == "m":
    cost += 20
elif size == "L" or size == "l":
    cost += 25
else:
    print("You typed the wrong inputs.")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y" or pepperoni == 'y':
    if size == "S" or size == "s":
        cost += 2
    else:
       cost += 3
elif pepperoni == "N" or pepperoni == "n":
    cost += 0
else:
    print("You typed the wrong inputs.")

cheese = input("Do you want extra cheese? Y or N: ")
if cheese == "Y" or cheese == "y":
    cost += 1
elif cheese == "N" or cheese == "n":
    cost += 0

print(f"Your final bill is: ${cost}.")


