a_val = float(input())
b_val = int(input())


def power_pos(a, n):
    if n > 1:
        return a * power(a, n - 1)
    elif n == 1:
        return a
    else:
        return 1


def power(a, n):
    if n > 0:
        return a * power_pos(a, n - 1)
    elif n == 0:
        return 1
    elif n < 0:
        return 1 / (a * power_pos(a, -n - 1))


result = power(a_val, b_val)
print(result)
