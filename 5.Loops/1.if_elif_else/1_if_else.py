a = int(input("Enter ur age : "))
print("Your age is ", a)


# Conditional Operators 
# 1. > greater than
# 2. < less than
# 3. >= greater than or equal to
# 4. <= less than or equal to
# 5. == equal to
# 6. != not equal to

# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)

if (a>=18):
    print("you can drive")
else:
    print("you cannot drive")
print("Yay!!!")

# Logical Operators
# 1. and
# 2. or
# 3. not

if (a>18 and a<100):
    print("you can drive")
elif(a==18):
    print("you are 18")
elif(a<18):
    print("you cannot drive")
else:
    print("you cannot drive")
