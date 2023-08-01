s = {1,3 ,5,7,8}
s1 = {2,3,4,5,6}
# print(s.union(s1))
# print(s.intersection(s1))
# print(s.difference(s1))
# print(s.symmetric_difference(s1))
# print(s.issubset(s1))
# print(s.issuperset(s1))
# print(s.isdisjoint(s1))
# print(s.copy())
# print(s)
# s.add(9)
# print(s)
# s.update(s1)

cities = {"tokyo", "Mumbai", "Pune "}
cities2 = {"tokyo", "Mumbai ", "Nashik", "Paris"}

cities.intersection_update(cities2)
print(cities)

cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities.difference_update(cities2)
print(cities)