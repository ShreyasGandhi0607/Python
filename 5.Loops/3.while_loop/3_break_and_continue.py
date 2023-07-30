# break statement 
# loop ko chod kar nikal jao 
for i in range(0,11):
    if(i == 10):
        break
    print("5 x ", i+1," = ", 5*(i+1))
print("the loop is terminated after 10 ")

# continue statement
# loop ko chod kar aage badh jao
for i in range(0,11):
    if(i == 5):
        print("Skip the iteration ")
        continue
    print("5 x ", i+1," = ", 5*(i+1))

