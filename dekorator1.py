import functools


def used_function_and_arguments(func):
    """
    Returns new function which prints used arguments and keyword arguments
    """
    @functools.wraps(func)
    def new_function(*args, **kwargs):
        print(f"Voláme funkci {func.__name__} s argumenty ({args}, {kwargs})")
        return func(*args, **kwargs)

    return new_function


@used_function_and_arguments
def fib(x):
    """
    Computes the x-th number of the Fibonacci sequence
    """
    if x <= 1:
        return x
    return fib(x - 1) + fib(x - 2)


@used_function_and_arguments
def addition(x, y):
    """
    Add two numbers
    """
    return x + y


if __name__ == "__main__":
    print(fib(2))
