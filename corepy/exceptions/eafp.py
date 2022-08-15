import os
import sys

try:
    # EAFP - easier to ask for forgiveness than for permission, hence do the work and catch the exception
    # do not do pre-emptive checks if the file exists
    os.open("/path/does/not/exist/file.dat", flags=1)
except OSError as e:
    print(f"Error: {e!r}", file=sys.stderr)  # FileNotFoundError(2, 'No such file or directory')
