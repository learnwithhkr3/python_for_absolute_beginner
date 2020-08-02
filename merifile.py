def squir(n):
    return n * n


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def table(n):
    t = []
    for i in range(1, 11):
        t.append(n * i)
    return t


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def dev(n1, n2):
    return n1 // n2
