marks = [3,5,"Shreyas",6,True]
print(marks)
print(type(marks))
print(marks[0])#positive index
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4]) 
print(marks[-4])#negative index
print(marks[-3])
print(marks[-2])
print(marks[-1])

print(marks[0:3])#slicing
print(marks[0:4])
print(marks[0:5])
print(marks[0:7])

print(marks[0:6])
#Jump Index
print(marks[0:6:2])

# same things applies for string as well
if 7 in marks:
    print("Yes")
else:
    print("No")

if "Shreyas" in marks:
    print("Yes")
else:
    print("No")


