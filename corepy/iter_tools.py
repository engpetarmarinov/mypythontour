import math
from itertools import islice, count, chain


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


# islice and count
thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(thousand_primes)  # <itertools.islice object at 0x102c1f0b0>
print(list(thousand_primes)[-10:])  # [7823, 7829, 7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901]

# any and all
print(any(is_prime(x) for x in range(7, 10)))  # True
print(all([True, True, False]))  # False

# zip
monday = [12, 12, 11, 8, 7, 6, 10, 12, 15, 16, 13, 12]
tuesday = [11, 11, 10, 8, 6, 6, 9, 11, 14, 15, 12, 12]
wednesday = [10, 10, 9, 8, 6, 6, 9, 10, 13, 14, 12, 11]

for temps in zip(monday, tuesday, wednesday):
    print(f"min={min(temps):4.1f}, max={max(temps):4.1f}, average={sum(temps) / len(temps):4.1f}")
"""
min=10.0, max=12.0, average=11.0
min=10.0, max=12.0, average=11.0
min= 9.0, max=11.0, average=10.0
min= 8.0, max= 8.0, average= 8.0
min= 6.0, max= 7.0, average= 6.3
min= 6.0, max= 6.0, average= 6.0
min= 9.0, max=10.0, average= 9.3
min=10.0, max=12.0, average=11.0
min=13.0, max=15.0, average=14.0
min=14.0, max=16.0, average=15.0
min=12.0, max=13.0, average=12.3
min=11.0, max=12.0, average=11.7
"""

# chain
temps = chain(monday, tuesday, wednesday)
print(all(t > 0 for t in temps))  # True
