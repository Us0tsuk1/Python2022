from math import sin, log


def main(y):
    if y < 99:
        return y
    elif y < 184:
        return pow(sin(y), 5) / 32
    elif y < 275:
        return pow(y, 6) / 87 - pow(y, 21) - 72 * pow(abs(pow(y, 2)), 3)
    elif y < 299:
        return pow((51 * y + 1 + 76 * pow(y, 3)), 7) * 83 + pow(log(y), 2) + 74
    else:
        return pow(y, 2) + 78 + pow(y, 4) * 49
