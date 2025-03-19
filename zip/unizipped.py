zipped = [(1, 'a'), (2, 'b'), (3, 'c')]

unzipped = zip(*zipped)

list1, list2 = unzipped
print(list1)  # Output: (1, 2, 3)
print(list2)  # Output: ('a', 'b', 'c')
