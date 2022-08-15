def generator123():
    yield 1
    yield 2
    yield 3


g = generator123()
print(g)  # <generator object generator123 at 0x1032d0190>

print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3

try:
    print(next(g))  # StopIteration exception
except StopIteration:
    pass


def lucas(stop):
    count = 1
    yield 2
    a = 2
    b = 1
    while True:
        if stop < count:
            break
        count += 1
        a, b = b, a + b
        yield b


print("Lucas sequence")
for i in lucas(100):
    print(i)

# generator expressions
hundred_squares = (x * x for x in range(1, 101))
print(hundred_squares)  # <generator object <genexpr> at 0x1010eb140>

# force the evaluation of the generator with list() and take the last 10
last = list(hundred_squares)[-10:]
print(last)

# sum squares of 1 million squares
print(sum(x * x for x in range(1, 1000001)))  # 333333833333500000
