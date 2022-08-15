# Container
# str, list, dict, range, tuple, set, bytes
container = [1, 2, 3]
2 in container

# Sized
# str, list, dict, range, tuple, set, bytes
len(container)

# Iterable - yields items one by one as they are requested
# str, list, dict, range, tuple, set, bytes
for item in container:
    print(item)

# Sequence - items can be referred by index
# str, list, range, tuple, bytes
item = container[0]
idx = container.index(2)
cnt = container.count(1)
reverse_iterator = reversed(container)

# Mutable Sequence
# list

# Mutable Set
# set

# Mutable Mapping
# dict
