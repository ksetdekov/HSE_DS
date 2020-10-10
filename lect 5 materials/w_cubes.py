import math

n_inp = int(input())
result = []


def c_root(k):
    """cube root calculator based on newton formula"""
    start = math.floor(len(str(k).encode('utf-8')) / 3) + 1
    x = start
    while True:
        x = (x - (x ** 3 - k) / (3 * x ** 2))//1
        if x ** 3 <= k < (x + 1) ** 3:
            break
    return int(x)


a_level = c_root(n_inp)
for a in range(a_level, -1, -1):
    b_inp = n_inp - a ** 2
    b_level = c_root(b_inp)
    # print(a, 'step a')
    if b_inp == 0:
        result.append(a)
        break
    # loop 1

    for b in range(b_level, -1, -1):
        c_inp = b_inp - b ** 2
        c_level = c_root(c_inp)
        # print(c_inp, 'step b')
        if c_inp == 0:
            result.append(b)
            break
            # loop 2

        for c in range(c_level, -1, -1):
            d_inp = c_inp - c ** 2
            d_level = c_root(d_inp)
            # print(d_inp, 'step d')
            if d_inp == 0:
                result.append(c)
                break
                # loop 3
            for d in range(d_level, 0, -1):
                e_inp = d_inp - d ** 2
                # print(e_inp, 'step e')
                if e_inp == 0 and len(result) == 0:
                    result.append(d)
                    break

                # end loop 3
            if len(result) != 0:
                result.append(c)
                break

            # end loop 2
        if len(result) != 0:
            result.append(b)
            break

    # end loop 1
    if len(result) != 0:
        result.append(a)
        break

if len(result) == 0:
    print('0')
else:
    print(*result)
