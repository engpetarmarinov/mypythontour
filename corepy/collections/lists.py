import copy

# negative indexes
r = [1, -4, 10, -16, 15]
print(r[-1])  # 15

# slicing a_list[start:stop]
s = [1, 2, 3, 4, 5]
print(s[1:3])  # [2, 3]
print(s[1:-1])  # [2, 3, 4] - except the last
print(s[2:])  # [3, 4, 5]
print(s[:2])  # [1, 2]

# copy list reference
copied_list = s[:]
print(copied_list is s)  # False
copied_list = s
print(copied_list is s)  # True

# copy - more readable
copied_list2 = s.copy()
print(copied_list2 is s)  # False
s[0] = 9
print(copy, copied_list2)  # [9, 2, 3, 4, 5] [1, 2, 3, 4, 5]

# copy with list constructor
copied_list3 = list(s)
print(copied_list3 is s)  # False
s[1] = 9
print(copied_list3)  # [9, 2, 3, 4, 5]

# shallow copy
a = [[1, 2], [3, 4]]
b = a.copy()
a[0].append(3)
print(f"a = {a}, b = {b}")  # a = [[1, 2, 3], [3, 4]], b = [[1, 2, 3], [3, 4]]

# deep copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
a[0].append(3)
print(f"a = {a}, b = {b}")  # a = [[1, 2, 3], [3, 4]], b = [[1, 2], [3, 4]]

# repetition operator
print([0] * 9)  # [0, 0, 0, 0, 0, 0, 0, 0, 0]

# index and count
w = "the quick brown fox jumps over the lazy dog".split()
i = w.index("fox")
print(i)  # 3
print(w.count("the"))  # 2

# test for membership
print(9 not in [1, 2, 3])  # True

# delete element by index
l = ["love", "python"]
del l[l.index("python")]
print(l)  # ['love']

# delete element by value
l = ["love", "python"]
l.remove("python")
print(l)  # ['love']

# insert
a = "I accidentally the whole universe".split()
a.insert(2, "destroyed")
print(" ".join(a))  # I accidentally destroyed the whole universe

# concat
print([1, 2, 3] + [4, 5, 7])  # [1, 2, 3, 4, 5, 6]
k = [1, 2, 3]
k.extend([4, 5, 6])
print(k)  # [1, 2, 3, 4, 5, 6]

# reverse
g = [1, 2, 3]
g.reverse()
print(g)  # [3, 2, 1]

# sort
g = [2, 5, 6, 7, 1, 3]
g.sort(reverse=True)
print(g)  # [7, 6, 5, 3, 2, 1]

# reversed
x = [4, 9, 2, 1]
reversed_list_iterator = reversed(x)
print(reversed_list_iterator)  # <list_reverseiterator object at 0x10496f640> <- wut?
print(list(reversed_list_iterator))  # [1, 2, 9, 4]

# sorted
x = [4, 9, 2, 1]
print(sorted(x))  # [1, 2, 4, 9]
