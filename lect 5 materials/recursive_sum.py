av = int(input())
bv = int(input())


def my_sum(a, b):
    if b == 0:
        return a
    else:
        b -= 1
        a += 1
        return my_sum(a, b)


print(my_sum(av, bv))
