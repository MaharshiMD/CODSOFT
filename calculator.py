print("Simple Calculator")

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("Calculator closed.")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            result = num1 + num2
            print("Result:", result)

        elif choice == "2":
            result = num1 - num2
            print("Result:", result)

        elif choice == "3":
            result = num1 * num2
            print("Result:", result)

        elif choice == "4":
            if num2 == 0:
                print("Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("Result:", result)

    else:
        print("Invalid choice. Please select between 1 to 5.")
