class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap


tracer = Trace()


@tracer
def rotate_list(list_to_rotate):
    return list_to_rotate[1:] + [list_to_rotate[0]]


if __name__ == "__main__":
    data = [1, 2, 3]
    data = rotate_list(data)  # Calling <function rotate_list at 0x1009900d0>
    print(data)  # [2, 3, 1]
    data = rotate_list(data)  # Calling <function rotate_list at 0x1009900d0>
    print(data)  # [3, 1, 2]
    tracer.enabled = False
    data = rotate_list(data)  # nothing printed, cause tracer is disabled
    print(data)  # [1, 2, 3]


