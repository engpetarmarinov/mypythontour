from functools import reduce


def mul(x, y):
    print(f"mul {x} and {y}")
    return x * y


def main():
    print(reduce(mul, range(1, 10)))
    """
    mul 1 and 2
    mul 2 and 3
    mul 6 and 4
    mul 24 and 5
    mul 120 and 6
    mul 720 and 7
    mul 5040 and 8
    mul 40320 and 9
    362880
    """

    # reduce with an initial param
    print(reduce(mul, [], 1))  # 1
    reduce(mul, [])  # TypeError: reduce() of empty iterable with no initial value


if __name__ == '__main__':
    main()
