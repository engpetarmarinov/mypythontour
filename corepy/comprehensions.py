# [expr(item) for item in iterable]
def generate_item(item):
    return len(item)


# list comprehension
words = "Why sometimes I have believed as many as six items before breakfast".split()
co = [generate_item(item) for item in words]

print(co)  # [3, 9, 1, 4, 8, 2, 4, 2, 3, 5, 6, 9]

"""
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

capital_to_country = {
    capital: country
    for country, capital in country_to_capital.items()
}
print(capital_to_country)  # {'Sofia': 'Bulgaria', 'London': 'United Kingdom', 'Rabat': 'Morocco'}

