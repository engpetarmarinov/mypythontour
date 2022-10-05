class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    def __new__(cls):
        print("SingletonClass.__new__ invoked")

    def __init__(self):  # Never called, cause __new__ is invoked first
        print("SingletonClass.__init__ invoked")


class RegularClass:
    pass


if __name__ == "__main__":
    x = SingletonClass()
    y = SingletonClass()
    print(x == y)  # True

    x = RegularClass()
    y = RegularClass()
    print(x == y)  # False
