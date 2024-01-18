a = [36, 7, 1, 90, 3, 28, 10]
b = [4, 2, 59, 3, 10, 15, 67, 33]
c =[]
d = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(c)
for i in a:
    for j in b:
        if i % j == 0:
            d.append(i)
print(d)