# Uppgift4.py
# Programmering 1 – Uppgift 4
# Function-Based Calculator

# --- Functions ---
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# Bonus: extra operationer
def power(x, y):
    return x ** y

def remainder(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x % y


# --- Program loop ---
while True:
    print("\n==== CALCULATOR ====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (bonus)")
    print("6. Remainder (bonus)")
    print("7. Quit")

    choice = input("Choose an option (1-7): ").strip()

    if choice == "7":
        print("Goodbye!")
        break

    if choice in ("1", "2", "3", "4", "5", "6"):
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(x, y))
            elif choice == "2":
                print("Result:", subtract(x, y))
            elif choice == "3":
                print("Result:", multiply(x, y))
            elif choice == "4":
                print("Result:", divide(x, y))
            elif choice == "5":
                print("Result:", power(x, y))
            elif choice == "6":
                print("Result:", remainder(x, y))

        except ValueError:
            print("Invalid input! Please enter numbers only.")
    else:
        print("Please choose a valid option (1–7).")
