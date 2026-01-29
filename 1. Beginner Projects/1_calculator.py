# Here is my simple calculator app.
# Here I used the class so that I can make this app modular and use whenever I want.
class Calculator:
    """
    Here is a simple calculator class to perform basic operations. 
    Methods:
        add(a,b): Returns the sum of two numbers.
        sub(a,b): Returns the subtraction of two numbers.
        mul(a,b): Returns the multiplication of two numbers.
        div(a,b): Returns the division of two numbers.
        Here in each function a and b are two parameters which are taken as the numbers.
    """
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b
    
def main():
    calc = Calculator()
    while True:
        """
        Here using the while loop basically keeps the calculator app running until the "q" value is passed inside the operation which breaks the loop and takes out of this application.
        """
        try:
            print("What kind of operation do you want to perform.\nPress + for addition\nPress - for the subtraction.\nPress * for multiplication.\nPress / for division.\nPress q to quit.")
            operation = input("Enter the Operation: ")
            
            o = operation.lower()
            if o=="q":
                print("Exiting the calculator. Bye")
                break
                
            a = float(input("Enter the first number: "))

            b = float(input("Enter the second number: "))
            
            match o:
                case "+":
                    print(f"The sum of {a} and {b} is {calc.add(a,b)}")
                case "-":
                    print(f"The subtraction between {a} and {b} is {calc.sub(a,b)}")
                case "*":
                    print(f"The product of {a} and {b} is {calc.mul(a,b)}")
                case "/":
                    if b == 0:
                        print("Error: Division by zero is not allowed.")
                    else:    
                        print(f"The division {a} by {b} is {calc.div(a,b)}")
                case _:
                    print("Enter the proper operation to perform the calculation.")
                    
        except Exception as e:
            print("Enter the valid number.")
            
if __name__ == "__main__":
    main()