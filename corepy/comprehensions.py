# [expr(item) for item in iterable]
def generate_item(item):
    return len(item)


# list comprehension
words = "Why sometimes I have believed as many as six items before breakfast".split()
co = [generate_item(item) for item in words]

print(co)  # [3, 9, 1, 4, 8, 2, 4, 2, 3, 5, 6, 9]

"""
Dictionary comprehension
{
    key_expr(item): value_expr(item)
    for item in iterable
}
"""
country_to_capital = {
    "Bulgaria": "Sofia",
    "United Kingdom": "London",
    "Morocco": "Rabat",
}

# dict comprehension
capital_to_country = {
    capital: country
    for country, capital in country_to_capital.items()
}
print(capital_to_country)  # {'Sofia': 'Bulgaria', 'London': 'United Kingdom', 'Rabat': 'Morocco'}

# filtering comprehensions
print([x for x in range(10) if x % 2 == 0])  # [0, 2, 4, 6, 8]

# generator comprehension
g = (i * 2 for i in range(1, 11))
print(type(g))  # <class 'generator'>
for v in g:
    print(v)
"""
2
4
6
8
10
12
14
16
18
20
"""

# multi input comprehensions
# cartesian product
print([(x, y) for x in range(5) for y in range(5)])
# [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]


# nested comprehensions
print([[y * 3 for y in range(x)] for x in range(10)])
# [[], [0], [0, 3], [0, 3, 6], [0, 3, 6, 9], [0, 3, 6, 9, 12], [0, 3, 6, 9, 12, 15], [0, 3, 6, 9, 12, 15, 18], [0, 3, 6, 9, 12, 15, 18, 21], [0, 3, 6, 9, 12, 15, 18, 21, 24]]
