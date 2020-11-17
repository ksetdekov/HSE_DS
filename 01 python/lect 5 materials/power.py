a_val = float(input())
b_val = int(input())


def power(a, n):
    if n > 1:
        return a * power(a, n - 1)
    elif n == 1:
        return a
    else:
        return 1


result = power(a_val, b_val)
print(result)
