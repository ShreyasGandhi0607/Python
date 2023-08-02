a = input("Enter the number : ")
print(f" Multiplication table of {a} is :")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} * {i} = {int(a)*i}")
# except Exception as e:
#     # print(e)
#     print("Invalid Input ")

# print("This is important line")
# print("End of Program")

try: 
    num = int(input("Enter the integer"))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer : ")
except IndexError:
    print("Enter index error ")

