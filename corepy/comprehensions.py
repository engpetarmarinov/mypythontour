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
