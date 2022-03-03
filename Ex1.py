from math import sqrt, pow, sin


def main(z, x):
    a = pow(abs(93 - pow(x, 2) - pow(z, 3)), 5)
    b = pow(pow(z, 3) + 1, 6)
    c = (pow(sin(x), 2) - (16 + pow(z, 2) + pow(x, 3)))
    d = (pow(x, 2) + pow(sin(z), 5))
    e = a + b
    result = sqrt(e) + c / d
    return result
