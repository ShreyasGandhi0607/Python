l = [13,2,53,4,25,6]
print(l)
l.append(8)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

l.pop()
print(l)

l.insert(2, 100)
print(l)

l.remove(100)
print(l)


print(l.count(3))
print(l.index(53))

m = [34, 56, 756543]
l.extend(m)
print(l) 