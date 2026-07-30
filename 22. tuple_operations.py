# tuples are immutable. if you want to change tuple items then first convert the tuple to a list then perform operations on that list and convert it back to tuple 

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
print(countries)

temp.append("Russia") #add item
print(temp)

temp.pop(3) #remove item
print(temp)

temp[2] = "Finland"
print(temp)

countries = tuple(temp)
print(countries)

#we can directly concatenate two tuples without converting them to a list

countries1 = ("India", "Pakistan")
countries2 = ("vietnam", "china")
asia = countries1 + countries2
print(asia)

# TUPLE METHODS

# 1. count() method
tuple1 = (0,1,2,3,1,2,3,3,4,5,3)
res = tuple1.count(3)
print("Count of 3 is:", res)

# 2. index() - first occurence of given element

res = tuple1.index(3)
print(res)
res = tuple1.index(3, 4, 8)
print(res)
# will raise value error if element is not present

res = len(tuple1)
print(res)
