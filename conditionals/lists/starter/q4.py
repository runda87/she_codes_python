a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

d.append(a)
d.append(b)
d.append(c)
print(d)
e.extend(a)
e.extend(b)
e.extend(c)
print(e)


#result
# Produce the following lists:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]