import functools


class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0
        # preserves f metadata like f.__doc__, but help(f) will still look at the CallCount class decorator
        functools.update_wrapper(self, f)

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    """Prints a hello message with a name."""
    print('Hello, {}!'.format(name))


if __name__ == "__main__":
    hello('Petar')
    hello('Ivan')
    hello('John')
    help(hello)  # hello = class CallCount(builtins.object)
    help(hello.__doc__)  # Prints a hello message with a name.
    print(hello.count)  # 3
