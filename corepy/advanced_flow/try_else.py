if __name__ == "__main__":
    try:
        filename = "test.txt"
        f = open(filename, "rt")
    except OSError:
        print(f"File {filename} could not be open for read.")
    else:
        # Now we are sure the file is open
        num_lines = sum(1 for line in f)
        print(f"Number of lines {num_lines}")
        f.close()
    finally:
        print("We are done")
