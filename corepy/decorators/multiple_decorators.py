from function_decorators import escape_unicode
from instance_decorators import Trace


tracer = Trace()


@tracer  # this is invoked second, then it invokes the bulgarian_mr_prefix
@escape_unicode  # this is invoked first, then it invokes tracer decorator
def bulgarian_mr_prefix(name):
    return f"Г-н {name}"


if __name__ == "__main__":
    unicode_escaped_name = bulgarian_mr_prefix("Маринов")  # Calling <function escape_unicode.<locals>.wrap at 0x1012d17e0>
    print(unicode_escaped_name)  # '\u0413-\u043d \u041c\u0430\u0440\u0438\u043d\u043e\u0432'
