import functools


def escape_unicode(f):  # decorators accept callable
    @functools.wraps(f)  # preserves the metadata
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap  # decorators return callable


@escape_unicode
def northern_city():
    """Returns Norwegian name of a city"""
    return "Tromsø"


if __name__ == "__main__":
    help(northern_city)  # northern_city() - the metadata is preserved by @functools.wraps(f)
    help(northern_city.__doc__)  # 'Returns Norwegian name of a city'
    print(northern_city())  # 'Troms\xf8'

