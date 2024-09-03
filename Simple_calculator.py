# CIS 103: Introduction to Programming
#Lab 02: "Building a Simple Calculator"
#Instructor: Md Ali
#Student Name: Sahar Iqbal
#Date: 09/02/2024

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    while True:
        # Display menu options
        print("\nPlease select an operation -")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            # Get user's choice
            operation = int(input("Select an operation (1, 2, 3, 4, 5): "))

            if operation == 5:
                print("Exiting the calculator. Goodbye!")
                break

            if operation in [1, 2, 3, 4]:
                # Get numbers from user
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))

                if operation == 1:
                    result = add(first_number, second_number)
                elif operation == 2:
                    result = subtract(first_number, second_number)
                elif operation == 3:
                    result = multiply(first_number, second_number)
                elif operation == 4:
                    result = divide(first_number, second_number)

                print(f"Result: {result}")
            else:
                print("Invalid input. Please select a valid operation (1, 2, 3, 4, 5).")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
