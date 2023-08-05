f = open("requirement.txt", 'r')
text  = f.read()
print(text )


f.close()

# WRITING A FILE

f = open('myfile.txt', 'a')
f.write('Hello, world!')
f.close()

with open('myfile.txt', 'a') as f:
    f.write("Hey I am inside with")
