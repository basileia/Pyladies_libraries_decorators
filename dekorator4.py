import functools


def google_link_exception(func):
    """
    Checks for an exceptions. If exception occurs it will provide a link
    to google search result
    """
    @functools.wraps(func)
    def new_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_string = repr(e)
            error_string = '+'.join(error_string.split())
            url = 'https://www.google.com/search?q=' + error_string + '&ie=utf-8&oe=utf-8'
            print("Došlo k chybě")
            return url

    return new_function


@google_link_exception
def division(a, b):
    """
    Divides two numbers
    """
    return a / b


if __name__ == "__main__":
    print(division(5, 0))
    print(division(100, 5))
