import sys

# IndexError
z = [1, 2, 3]
try:
    z[4]
except IndexError as e:
    print(f"{e!r}", file=sys.stderr)  # IndexError('list index out of range')


# ValueError
try:
    int("jim")
except ValueError as e:
    print(f"{e!r}", file=sys.stderr)  # ValueError("invalid literal for int() with base 10: 'jim'")


# KeyError
try:
    d = dict(a=1, b=2, c=3)
    d['d']
except KeyError as e:
    print(f"{e!r}", file=sys.stderr)  # KeyError('d')
