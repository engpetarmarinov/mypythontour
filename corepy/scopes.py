count = 0


def show_count():
    print(count)


def set_count(c):
    count = c  # shadowing


def set_global_count(c):
    global count
    count = c


def main():
    show_count()  # 0
    set_count(5)
    show_count()  # 0
    set_global_count(5)
    show_count()  # 5


if __name__ == '__main__':
    main()
