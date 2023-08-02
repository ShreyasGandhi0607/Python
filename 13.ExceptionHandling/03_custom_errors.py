a = input("Enter the value beetween 5 and 9 : ")
try:
    if(int(a)<5 or int(a)>9):
        raise ValueError("Value should be between 5 and 9 ")
# in python we can build custom errors by using < raise > keyword
except:
    if a== str(a) or a == "quit " :
        raise ValueError("Quit word is defined")

