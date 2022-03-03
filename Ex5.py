from math import ceil, atan


def main(z):
    n = len(z)
    result = 0
    for i in range(1, n + 1):
        result += 9 * pow(atan(z[n - ceil(i / 3)]), 2)
    return result * 82

