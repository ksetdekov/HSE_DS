a_val = int(input())
b_val = int(input())


def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def reduce_fraction(n, m):
    divider = gcd(n, m)
    return int(n / divider), int(m / divider)


result = reduce_fraction(a_val, b_val)
print(*result)
