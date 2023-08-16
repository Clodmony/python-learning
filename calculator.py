def addition(x, y):
    return x + y

def substraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def dividation(x, y):
    if y == 0:
        return ('Can not divide by zero!') 
    return x / y

while True:
    print('Select operation.')
    print('1. Addition')
    print('2. Substraction')
    print('3. Multiplication')
    print('4. Dividation')
    print('5. Exit')

    userinput = input(": ")

    if userinput in ("Addition", "Substraction", "Multiplication", "Dividation", "Exit"):
        while True:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input, please enter a number!")

        if userinput == "Addition":
            print(x, "+", y, "=", addition(x, y))
        elif userinput == "Substraction":
            print(x, "-", y, "=", substraction(x, y))
        elif userinput == "Multiplication":
            print(x, "*", y, "=", multiplication(x, y))
        elif userinput == "Dividation":
            print(x, "/", y, "=", dividation(x, y))
        elif userinput == "Exit":
            break

print("Thank you for using calculator!")
