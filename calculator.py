# print("hello world")

class Calculator:

    # class AddSub:
        def __init__(self):
            pass

        def addition(self, x, y):
            return x + y
    
        def subtraction(self, x, y):
            return x - y
        
    # class MulDiv:
        def __init__(self):
            pass

        def multiplication(self, x, y):
            return x * y
        
        def division(self, x, y):
            if y == 0:
              return "Error!"
            else:
                return x / y
            
def main():
    calculator = Calculator()
    print("Welcome to my Calculator")
    print("press 1 to add")
    print("press 2 to subtract")
    print("press 3 to multiply")
    print("press 4 to divide")
    print("press 5 to exit")


    while True:
        num = input("Enter a number from 1-5:")

        if num in ("1", "2", "3", "4"):
            num1 = float(input("Input the first number: "))
            num2 = float(input("Input the second number: "))

            if num == "1":
                print("The result is:", calculator.addition(num1, num2))
            elif num == "2":
                print("The Result is:", calculator.subtraction(num1, num2))
            elif num == "3":
                print("The Result is:", calculator.multiplication(num1, num2))
            elif num == "4":
                print("The Result is:", calculator.division(num1, num2))

        elif num == "5":
            print("The End.")
            break
        else:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()


# calc1 = Calculator()
# calc1.__init__()

# print(calc1)

