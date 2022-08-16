import sys

# writing into a file
try:
    f = open("wasteland.txt", mode="wt", encoding="utf-8")
    f.write("What's going on?\n")
    f.write("Am I writing into a file?\n")
finally:
    f.close()

# reading from a file
try:
    f = open("wasteland.txt", mode="rt", encoding="utf-8")
    for line in f:
        sys.stdout.write(line)
finally:
    f.close()

# appending to a file
try:
    f = open("wasteland.txt", mode="at", encoding="utf-8")
    f.writelines([
        "This line was appended!\n",
        "This line was appended too!\n",
    ])
finally:
    f.close()


# with-block will implicitly close the file.
with open("wasteland.txt", mode="at", encoding="utf-8") as f:
    f.writelines([
        "Add some more lines from within a with-block.\n",
    ])
