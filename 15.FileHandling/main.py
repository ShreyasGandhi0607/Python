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


# READING A FILE
# LINE BY LINE
f = open('myfile.txt', 'r')
for line in f:
    print(line)
f.close()

# ALL AT ONCE
f = open('myfile.txt', 'r')
text = f.read()
print(text)
f.close()

# methods in file 
# f.read()
# f.readline()
# f.readlines()
# f.write()
# f.close()
# f.tell()
# f.seek()
# f.closed
# f.mode
# f.name
# f.encoding
# f.errors
# f.fileno()
# f.flush()
# f.isatty()
# f.line_buffering()
# f.newlines


        