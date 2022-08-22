def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap


@escape_unicode
def northern_city():
    return "Tromsø"


if __name__ == "__main__":
    print(northern_city())  # 'Troms\xf8'

