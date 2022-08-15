# empty set
p = set()
print(p)  # set()

# sets contain unique values and duplicated items are discard
p = {1, 2, 3, 3, 4, 5, 5}
print(p)  # {1, 2, 3, 4, 5}

# common usage is to remove duplicates
p = [176, 876, 82, 876, 9, 3]
p = set(p)
print(p)  # {3, 9, 876, 176, 82}

# sets are iterable
for i in p:
    print(i)
"""
3
9
876
176
82
"""

# add items
p.add(7)
print(p)  # {3, 7, 9, 876, 176, 82}

# add multiple elements with update
p.update([8, 9, 10])
print(p)  # {3, 7, 8, 9, 10, 876, 176, 82}

