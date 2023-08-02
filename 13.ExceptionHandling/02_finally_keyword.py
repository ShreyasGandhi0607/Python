try:
    l = [2,5,6,3]
    i = int(input("Entr the index"))
    print(l[i])
except:
    print(" Some error occured")
finally:
    print("This is finally block, it is always executed")

# The block of code written inside finally clause is
#  executed always irrespective of the retun of the values from try or except
#  blocks in a function. This fianlly clause may be used for various purposes 
# like closing some resourse files, closing the database connections or ending 
# the program with some appreciative messages.
