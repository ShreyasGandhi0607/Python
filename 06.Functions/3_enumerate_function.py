marks = [34, 56 ,67 , 97, 45 , 45]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Awesome Shreyas")
#     index+=1

# instead using enumerate function
for index,mark in enumerate(marks,start = 1):
    print(mark)
    if(index == 3):
        print("Awesome Shreyas")
    index+=1

