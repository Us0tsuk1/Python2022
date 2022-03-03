def main(n):
    if n == 0:
        return 0.33
    if n > 1:
        return pow(main(n - 2), 9) - main(n - 1) - pow(main(n - 2), 2) / 56
    return 0.16

