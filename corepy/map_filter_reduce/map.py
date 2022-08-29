import itertools


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, **kwargs)

        return wrap


def main():
    # Map is lazy, it will return iterable
    result = map(Trace()(ord), "The quick brown fox")
    print(result)  # <map object at 0x104d2b3d0>

    print(next(result))  # Calling <built-in function ord>
    # 84
    print(next(result))  # Calling <built-in function ord>
    # 104

    for o in result:
        print(o)

    sizes = ['small', 'medium', 'large']
    colors = ['lavender', 'teal', 'burnt orange']
    animals = ['koala', 'platypus', 'salamander']

    def combine(quantity, size, color, animal):
        return f"{quantity} x {size} {color} {animal}"

    print(list(map(combine, itertools.count(), sizes, colors, animals)))
    # ['0 x small lavender koala', '1 x medium teal platypus', '2 x large burnt orange salamander']


if __name__ == '__main__':
    main()
