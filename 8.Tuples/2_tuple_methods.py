countries = ("Spain", "Italy", "India", "USA", "Germany")

temp = list(countries)
temp.append("Russia")
countries = tuple(temp)
print(countries)
temp.pop(3)
countries = tuple(temp)
print(countries)


tuple1 = (1,3,4,5,6,7)
res = tuple1.count(3)
print("Count of 3 in tuple1 is ", res)
