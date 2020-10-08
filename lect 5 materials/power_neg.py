a_val = float(input())
b_val = int(input())

def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / a * power(a, -n)
    elif n % 2 == 1:
        return power(a, n - 1) * a
    else:
        return power(a, n // 2) ** 2

result = power(a_val, b_val)
print(result)
