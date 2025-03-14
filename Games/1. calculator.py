# This is my calculator app.

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y != 0:
            return x/y
        return
        
def main():
    calc = Calculator()
    while True:
        print("\n Select the operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        choice = int(input("Enter the number: "))
        
        if choice == 5:
            print("Exiting the calculator. Good bye!")
            break
    
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        
        if choice == 1:
            print(f"The sum of {num1} and {num2} is {calc.add(num1, num2)}")
        elif choice == 2:
            print(f"The differene of {num1} and {num2} is {calc.subtract(num1, num2)}")
        elif choice == 3:
            print(f"The product of {num1} and {num2} is {calc.multiply(num1, num2)}")
        elif choice == 4:
            print(f"The division of {num1} and {num2} is {calc.divide(num1, num2)}")
        else:
            print("Invalid number.")
        
if __name__ == "__main__":
    main()