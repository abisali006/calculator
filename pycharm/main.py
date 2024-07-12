from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def main():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator!")
                continue

            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

        quit = input("Do you want to quit? (Y for yes, N for no): ").strip().lower()
        if quit == 'y':
            break

if _name_ == "_main_":
    main()