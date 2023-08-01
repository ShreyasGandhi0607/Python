# dictioneries are combination of key - value pairs 

dic = {
    121 : "Shenaz",
    122 : "Shreyas",
    123 : "Parth"
}

print(dic)
print(dic[121])
print(dic.get(121))

for key in dic.keys():
    print(f"Value correspomding to key {key} id {dic[key]}")

print(dic.items())