import math
import datetime

# concat
print("new" + "found" + "land")  # newfoundland

s = "new"  # new immutable object string "new"
s += "found"  # new immutable object string "found" and new immutable object string "newfound"
s += "land"  # new immutable object string "land" and new immutable object string "newfoundland"
# "new", "found" and "land" are left unreferenced, GC will take care
print(s)  # newfoundland

# join is more efficient to concat
print(''.join(["new", "found", "land"]))  # newfoundland

colors = ';'.join(['#333', '#666', '#000'])
print(colors)  # #333;#666;#000

# split
print(colors.split(';'))  # ['#333', '#666', '#000']

# partition - useful for unpacking tuples
print("unforgetable".partition("forget"))  # ('un', 'forget', 'able')

departure, separator, arrival = "London:Edinburgh".partition(':')
print(departure, separator, arrival)  # London : Edinburgh

# format
print("The age of {} is {}".format('Jim', 32))  # The age of Jim is 32
print("The age of {name} is {age}".format(age=32, name='Jim'))  # The age of Jim is 32
print("Math constants: pi={m.pi}, e={m.e}".format(m=math))  # Math constants: pi=3.141592653589793, e=2.718281828459045
print("Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))  # Math constants: pi=3.142, e=2.718

# literal string interpolation
print(f"one plus one is {1 + 1}")  # one plus one is 2
print(f"The current time is {datetime.datetime.now().isoformat()}")  # The current time is 2022-08-11T15:11:00.558841

