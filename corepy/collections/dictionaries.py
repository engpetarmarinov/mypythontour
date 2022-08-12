from pprint import pprint as pp

# convert list with tuples to dictionary
names_and_ages = [
    ("Alice", 32),
    ("Bob", 48),
    ("Charlie", 28),
    ("Daniel", 33),
]

d = dict(names_and_ages)
print(d)  # {'Alice': 32, 'Bob': 48, 'Charlie': 28, 'Daniel': 33}

# shallow copy
d = dict(goldenrod=0xDA520, indigo=0x4B0082)
e = d.copy()
f = dict(e)
print(f)  # {'goldenrod': 894240, 'indigo': 4915330}

# update
r = dict(indigo=0x4B0083, wheat=0xF5DEB3)
r.update(d)
print(r)  # {'indigo': 4915330, 'wheat': 16113331, 'goldenrod': 894240}

# iterate
for i in r:
    print(f"key: {i}, value: {r[i]}")
"""
key: indigo, value: 4915330
key: wheat, value: 16113331
key: goldenrod, value: 894240
"""

# iterate values
for value in r.values():
    print(f"value: {value}")

# iterate items
for key, value in r.items():
    print(f"key: {key}, value: {value}")
"""
key: indigo, value: 4915330
key: wheat, value: 16113331
key: goldenrod, value: 894240
"""

# delete
del r["indigo"]
print(r)  # {'wheat': 16113331, 'goldenrod': 894240}
pp({"A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]})
