def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)


def sum_series(n, b=0, c=1):
    if (b == 0 and c == 1):
        return fibonacci(n)
    elif (b == 2 and c == 1):
        return lucas(n)
    else:
        return fibonacci(n)+lucas(n)
