from math import pow, sin


def main(b, z, n, m):
    result = 0
    for j in range(b):
        result += pow(j, 6) / 92 - 31 - 22 * z
    for c in range(1, m + 1):
        product = 1
        for j in range(1, n + 1):
            temp = 0
            for i in range(1, b + 1):
                temp += pow(abs(93 - pow(z, 2) - pow(j, 3)), 7) \
                        - pow(pow(i, 3) + 1, 3) - pow(sin(c), 2)
            product *= temp
        result -= product
    return result
