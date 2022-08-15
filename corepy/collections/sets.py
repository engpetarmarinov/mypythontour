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

# set algebra - union, difference, intersection, subset, superset, disjoint
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia'}

# union
print(blond_hair.union(blue_eyes))  # {'Jack', 'Amelia', 'Mia', 'Olivia', 'Lily', 'Harry'}
print(blond_hair.union(blue_eyes) == blue_eyes.union(blond_hair))  # True

# difference
print(blond_hair.difference(blue_eyes))  # {'Amelia', 'Mia'}
print(blue_eyes.difference(blond_hair))  # {'Olivia', 'Lily'}

# symmetric difference - people with blue eyes or blond hair, but not both
print(blond_hair.symmetric_difference(blue_eyes))  # {'Amelia', 'Lily', 'Mia', 'Olivia'}

# intersection
print(blond_hair.intersection(blue_eyes))  # {'Jack', 'Harry'}

# subset
print({2, 3, 4}.issubset({1, 2, 3, 4, 5}))  # True

# superset
print({1, 2, 3, 4, 5}.issuperset({2, 3, 4}))  # True

# disjoint
print({1, 2, 3, 4, 5}.isdisjoint({6, 7, 8}))  # True
