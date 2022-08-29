def main():
    # filter is lazy and will return iterable
    positives = filter(lambda x: x > 0, [-1, 0, 2, 3, -4, -2])
    print(positives)  # <filter object at 0x101293280>
    for pos in positives:
        print(pos)  # 2 and 3


if __name__ == '__main__':
    main()
