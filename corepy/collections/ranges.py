print(range(5))  # range(0, 5)

for i in range(5):
    print(i)  # 01234

print(list(range(5, 10)))  # [5, 6, 7, 8, 9]

print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]

t = [1, 2, 3, 4, 5]

for p in enumerate(t):
    print(p)
"""
(0, 1)
(1, 2)
(2, 3)
(3, 4)
(4, 5)
"""

for i, v in enumerate(t):
    print(f"i = {i}, v = {v}")
"""
i = 0, v = 1
i = 1, v = 2
i = 2, v = 3
i = 3, v = 4
i = 4, v = 5
"""