tup = (1, 2, 3, "red", True)
print(type(tup), tup)

# tuples cannot be changed
# tup[0] = 10

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
# print(tup[5])

if 3 in tup:
    print("present")

tup2 = tup[1:4]
print(tup2)