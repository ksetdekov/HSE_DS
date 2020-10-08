a_val = float(input())
b_val = int(input())

def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        res = 1
        while n > 0:
            res *= a
            n -= 1
        return res
    elif n < 0:
        n = -n
        res = 1
        while n > 0:
            res *= a
            n -= 1
        return 1/res


result = power(a_val, b_val)
print(result)
