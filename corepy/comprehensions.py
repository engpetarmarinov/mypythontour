# [expr(item) for item in iterable]
words = "Why sometimes I have believed as many as six items before breakfast".split()
co = [len(item) for item in words]

print(co)  # [3, 9, 1, 4, 8, 2, 4, 2, 3, 5, 6, 9]
