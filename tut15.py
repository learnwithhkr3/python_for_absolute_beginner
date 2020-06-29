l = [["banana",40],["apple",30],["mango",50]]

# print(l[0])
# print(l[1])
# print(l[2])

d = dict(l)
for item, price in d.items():
    if price >= 40:
        print(item,price)
    