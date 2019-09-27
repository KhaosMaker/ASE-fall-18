# Calculator.py


def sum(m, n):
    s = sign(n)
    for i in range(abs(n)):
        m += s
    return m


def divide(m, n):
    assert n != 0, "Error: can't divide by 0!"
    s = sign(m) * sign(n)
    m = abs(m)
    n = abs(n)
    res = 0
    while m >= n:
        m -= n
        res += 1
    return res*s


def subtract(m, n):
    return sum(m, -n)


def multiply(m, n):
    res = 0
    s = sign(m)*sign(n)
    for i in range(abs(n)):
        res = sum(res, m)
    return res*s


def sign(n):
    return 1 if n >= 0 else -1
