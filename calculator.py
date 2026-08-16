# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Subtraction")
print("2. Multiplication")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    result = num1 - num2
    print("Subtraction =", result)

elif choice == "2":
    result = num1 * num2
    print("Multiplication =", result)

else:
    print("Invalid choice")