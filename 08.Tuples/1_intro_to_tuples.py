# similiar to list only difference is that tuples cannot be changed

# Tuples are immutable
# Tuples are ordered
# Tuples are indexed
# Tuples are iterable
# Tuples are hashable
# Tuples are comparable

tup = (1,3, "Green")
# tup[0] = 90
print((tup), tup)

print(tup[0])

if 6 in tup:
    print("Yes")
else:
    print("No")


# Slicing

tup2 = tup[1:3]
print(tup2)