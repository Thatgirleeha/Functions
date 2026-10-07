#building a calculator using functions
print("Welcome to my Calculator")
print("Select an operation to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
#functions
def addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def  Multiplication(a,b):
    return a*b
def Division(a,b):
    return a/b
#program loop
while True:
    choice=input("Enter the opereation to perform:").lower()
    if choice=="5":
        print("Closing the calculator...........")
        break
    elif choice in ["1","2","3","4"]:
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        if choice=="1":
            print("Result;", addition(num1, num2))#functioncall
        elif choice=="2":
            print("Result;", Subtraction(num1, num2))#functioncall
        elif choice=="3":
            print("Result;", Multiplication(num1, num2))#functioncall
         
        elif choice=="4":
                    print("Result;", Division(num1, num2))#functioncall
    else:
         print("Invalid choice. Please select option 1,2,3,4, or 5.")