class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_numbers(self):
        # Function to get two numbers from the user
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))

    def addition(self):
        # Function to perform addition
        return self.num1 + self.num2

    def subtraction(self):
        # Function to perform subtraction
        return self.num1 - self.num2

    def multiplication(self):
        # Function to perform multiplication
        return self.num1 * self.num2

    def division(self):
        # Function to perform division
        if self.num2 == 0:
            return "Cannot divide by zero"
        else:
            return self.num1 / self.num2

def main():
    calc = Calculator()

    while True:
        # Get numbers from the user
        calc.get_numbers()

        while True:
            # Menu for calculator operations
            print("1. ADDITION")
            print("2. SUBTRACTION")
            print("3. MULTIPLICATION")
            print("4. DIVISION")
            print("5. Quit")

            # Get user choice
            choice = input("Enter your choice: ")

            if choice == '1':
                result = calc.addition()
                print("Result:", result)
            elif choice == '2':
                result = calc.subtraction()
                print("Result:", result)
            elif choice == '3':
                result = calc.multiplication()
                print("Result:", result)
            elif choice == '4':
                result = calc.division()
                print("Result:", result)
            elif choice == '5':
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    main()
