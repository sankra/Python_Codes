list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10, 20, 30]

# Zip the lists together
zipped = zip(list1, list2, list3)

# Convert the zipped object to a list of tuples
result = list(zipped)

print(result)
