a = [1, 2, 3, 4]
b = []
print(id(a))
print(id(b))
b = a
print(id(a))
print(id(b))
b.append('f')
print(a)
print(b)