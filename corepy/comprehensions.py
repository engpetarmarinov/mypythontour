# [expr(item) for item in iterable]
def generate_item(item):
    return len(item)


words = "Why sometimes I have believed as many as six items before breakfast".split()
co = [generate_item(item) for item in words]

print(co)  # [3, 9, 1, 4, 8, 2, 4, 2, 3, 5, 6, 9]
