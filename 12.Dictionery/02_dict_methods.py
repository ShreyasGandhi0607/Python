emp = {
    121 : "Shenaz",
    122 : "Shreyas",
    123 : "Parth",
    124 : "John"
}

emp2 = {
    125 : "Rahul",
    126 : "Raj",
    127 : "Rohan"
}

# print(emp)
# print(emp2)

emp.update(emp2)
print(emp)

print(emp.keys())
print(emp.values())
print(emp.items())
emp.pop(121)
print(emp)
emp.popitem()
print(emp)
# emp.clear()
# print(emp)
# del emp
# print(emp)
# print(emp2)
# print(emp2.get(121))
# print(emp2.get(121, "Not Found"))