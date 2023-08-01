# def average(a=9,b=1):
#     avg = (a+b)/2
#     print(avg)

# average()#default arguments
# average(5,6)
# average(5)#default arguments

def name(fname, mname = "John ", lname = "Watson"):
    print("Hello ", fname , lname ,mname )
    print("\n")

name("Sherlock")#keyword arguments

# fname is required argument 

def average(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    avg = sum/len(numbers)
    # print("The average of ", numbers ," is ",avg)
    return avg


c = average(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(c)


def name(**name):
    print(type(name))
    print("Hello ", name["fname"], name["mname"], name["lname"])

name(mname = "BAchhan", lname = " Ganbura", fname = "Sinchan")
