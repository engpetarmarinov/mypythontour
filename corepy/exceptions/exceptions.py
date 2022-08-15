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
        x = int(number)
    except (KeyError, TypeError):
        x = -1
    return x


print(convert("three two".split()))  # 32
print(convert("around two trillions".split()))  # -1 -> KeyError
print(convert(23))  # -1 -> TypeError
