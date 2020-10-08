a_val = int(input())
b_val = int(input())


def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


result = gcd(a_val, b_val)
print(result)
