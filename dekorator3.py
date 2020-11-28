import functools


def check_zero_division(func):
    """Checks for division by zero"""
    @functools.wraps(func)
    def inner_function(x, y):
        try:
            return func(x, y)
        except ZeroDivisionError:
            print("Nulou dělit nemůžeš!")
            return

    return inner_function


@check_zero_division
def division(a, b):
    """Divides two numbers"""
    return a / b


if __name__ == "__main__":
    result = division(5, 0)
    if result:
        print("Výsledek dělení je:", result)
