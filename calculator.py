def calculator():
    while True:
        print("calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Enter choice (1-4): ")
        a = int(input("Enter first number : "))
        b = int(input("Enter second number: "))

        match choice:
            case "1":
                result = a + b
            case "2":
                result = a - b
            case "3":
                result = a * b
            case "4":
                result = a / b
            case _:
                print("Invalid choice, try again.")
                continue

        print("Result =", result)

calculator()