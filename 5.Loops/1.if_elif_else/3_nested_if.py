num = 18 
if (num<0):
    print("Negative")
elif(num>0):
    if(num<10 ):#nested if statement 
        print("Single digit positive number")
    elif(num<100):
        print("Double digit positive number")
    else:
        print("Triple digit positive number")
else:
    print("Zero")

