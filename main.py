from utils import * 
while True:
    operation = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit): ").lower()
    if operation == "exit":
        break

    elif operation == "add":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        resultado = add(num1, num2)

    elif operation == "subtract":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        resultado = sub(num1, num2)

    elif operation == "multiply":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        resultado = multiply(num1, num2)

    elif operation == "divide":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        resultado = divide(num1, num2)

    elif operation == "exponent":
        base = float(input("Enter the base number: "))
        exp = float(input("Enter the exponent: "))
        resultado = exponent(base, exp)

    elif operation == "modulo":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        resultado = modulo(num1, num2)

    elif operation == "floor_divide":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        resultado = floor_divide(num1, num2)

    elif operation == "absolute":
        num = float(input("Enter the number: "))
        resultado = absolute(num)

    else:
        print("Invalid option!")
        continue

    print(f"The result is: {resultado}")