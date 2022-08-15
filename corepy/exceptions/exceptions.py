import sys

DIGITAL_MAP = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'sever': 7,
    'eight': 8,
    'nine': 9,
}


def convert(s):
    try:
        number = ''
        for token in s:
            number += str(DIGITAL_MAP[token])
        return int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}", file=sys.stderr)
        return -1


print(convert("three two".split()))  # 32
print(convert("around two trillions".split()))  # -1 -> Conversion error: KeyError('around')
print(convert(23))  # -1 -> Conversion error: TypeError("'int' object is not iterable")
# Generally don't catch TypeError
