t = ("Norway", 4.953, 3)
print(len(t))  # ("Norway", 4.953, 3)

for item in t:
    print(item)

t2 = t + (33213.0, 265e9)
print(t2)  # ('Norway', 4.953, 3, 33213.0, 265000000000.0)

nested_tuple = ((1, 2), (3, 4))
print(nested_tuple[1][1])  # 4

tuple_with_no_brackets = 1, 2, 3, 4, 5

print(type(tuple_with_no_brackets))  # <class 'tuple'>


def minmax(items):
    return min(items), max(items)


print(minmax([83, 33, 84, 32, 85, 31, 86]))  # (31, 86)

# unpacking
lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])

print(lower, upper)  # 31 86

# tuple constructor
print(tuple("hello"))  # ('h', 'e', 'l', 'l', 'o')

# swapping
a = "jelly"
b = "fish"
a, b = b, a
print(a, b)  # fish jelly
