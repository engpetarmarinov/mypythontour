import functools


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap


tracer = Trace()


@tracer
def rotate_list(list_to_rotate: list) -> list:
    """ Rotates the first element of a list to the last place on the list

    :param list_to_rotate: a list to be rotated
    :return: the rotated list - the first element went on the last place
    """
    return list_to_rotate[1:] + [list_to_rotate[0]]


if __name__ == "__main__":
    help(rotate_list)  # prints the preserved docstring from the rotate_list func, not the decorator
    data = [1, 2, 3]
    data = rotate_list(data)  # Calling <function rotate_list at 0x1009900d0>
    print(data)  # [2, 3, 1]
    data = rotate_list(data)  # Calling <function rotate_list at 0x1009900d0>
    print(data)  # [3, 1, 2]
    tracer.enabled = False
    data = rotate_list(data)  # nothing printed, cause tracer is disabled
    print(data)  # [1, 2, 3]
