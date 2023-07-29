print("Enter the first number ")
num1 = input()
print("Enter the second number ")
num2 = input()

ch =0
while(ch != 5):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    print("Enter your choice ")
    ch = int(input())

    if(ch == 1):
        print("Addition of two numbers is ", int(num1)+int(num2))
    elif(ch == 2):
        print("Subtraction of two numbers is ", int(num1)-int(num2))
    elif(ch == 3):
        print("Multiplication of two numbers is ", int(num1)*int(num2))
    elif(ch == 4):
        print("Division of two numbers is ", int(num1)/int(num2))
    elif(ch == 5):
        exit()
    else:
        print("Invalid choice")