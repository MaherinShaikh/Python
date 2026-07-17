# append
l = [1, 2, 3, 4]
print(l)
l.append(5)
print(l)

#sort()
li = [23, 12, 9, 3, 5, 10,3,3]
li.sort()
print(li)
li.sort(reverse=True)
print(li)

#reverse()
li.reverse()
print(li)

#index() - returns index of first occurrence of list item
print(li.index(9))

#count() - returns count of number of items with the given value
print(li.count(3))

#copy()- returns copy of the list. done to perform operations without modifying the original list
m = li.copy()
m[0] = 0
print(li)
print(m)

#insert() - inserts an item at the given index. specify the index and the item to be inserted
li.insert(1,900)
print(li)

#extend() - This method adds an entire list or any other collection datatype:set,tuple,dictionary to an existing list
m = [200, 300, 400]
li.extend(m)
print(li)

k = li + m
print(k)