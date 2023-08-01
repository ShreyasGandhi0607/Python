# Time module execution 

import time
# timestamp = time.strftime("%H:%M:%S")
# print(timestamp)

timestamp = int(time.strftime('%H'))
print(timestamp)

if (timestamp>=0 and timestamp<12):
    print("Good Morning")
elif(timestamp>=12 and timestamp<16):
    print("Good Afternoon")
elif(timestamp>=16 and timestamp<20):
    print("Good Evening")
else:
    print("Good Night")




