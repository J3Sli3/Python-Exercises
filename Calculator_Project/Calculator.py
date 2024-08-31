import Art
def add(n1 : float, n2 : float) -> float:
        result = float(n1) + float(n2)
        return result
    
def multiply(n1 : float, n2 : float) -> float:
    result = float(n1) * float(n2)
    return result
    
def substraction(n1 : float, n2 : float) -> float:
    result = float(n1) - float(n2)
    return result
    
def divide(n1 : float, n2 : float) -> float:
    result = float(n1) / float(n2)
    return result

def calculator():
    print(Art.logo)
    first_number = float(input("What's the first number?: "))
    cont = True
    while cont == True:
        print(" + \n - \n * \n /")
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        
        if operation == "+":
            result = add(first_number, next_number)

        elif operation == "-":
            result = substraction(first_number, next_number)
        
        elif operation == "*":
            result = multiply(first_number, next_number)

        elif operation == "/":
            result = divide(first_number, next_number)

        
            
        print(f"{float(first_number)} {operation} {float(next_number)} = {float(result)} ")

        proceed = input(f"Type 'y' to continue calculating with {float(result)}, or type 'n' to start a new calculation: "  ).lower()

        if proceed == "y":
            first_number = float(result)

        elif proceed == "n":
            print("\n" * 100)
            calculator()

        else:
            print("\n" * 100)
            print("Uh... OH! Wrong Input... Let's Restart the calculator...")
            calculator()
            
calculator()




