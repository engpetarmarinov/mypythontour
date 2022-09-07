class MyClass:
    b = "on class"

    def __init__(self):
        self.a = "on instance"
        print(self.a)  # on instance - access instance attribute
        print(MyClass.b)  # on class - access class attribute
        print(self.b)
        # on class - access class attribute via instance attribute, instance attribute b will be implicitly created
        self.a = "re-bound"  # rebinds the existing a instance attribute
        self.b = "new on instance"
        print(self.b)  # new on instance
        print(MyClass.b)  # on class


def main():
    my_class = MyClass()


if __name__ == "__main__":
    main()
