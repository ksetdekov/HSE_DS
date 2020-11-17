def integer_sqrt(n):
    if n < 0:
        raise ValueError("works on non-negative")
    elif n < 2:
        return n
    else:
        small_candidate = integer_sqrt(n >> 2) << 1
        large_candidate = small_candidate + 1
        if large_candidate * large_candidate > n:
            return small_candidate
        else:
            return large_candidate


n_inp = int(input())

result = []
while n_inp > 0:
    result.append(integer_sqrt(n_inp))
    n_inp = - integer_sqrt(n_inp) ** 2 + n_inp
print(*result)

# todo нужно рекурсивно идти для каждого из вариантов первой разбивки - не брать максимум, а перебирать все,
# как ice cream
