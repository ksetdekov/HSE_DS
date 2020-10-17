import math


# n_inp = int(input())


def c_root(k):
    """cube root calculator based on newton formula"""
    start = math.floor(len(str(k).encode('utf-8')) / 3) + 1
    x = start
    while True:
        x = (x - (x ** 3 - k) / (3 * x ** 2)) // 1
        if x ** 3 <= k < (x + 1) ** 3:
            break
    return int(x)


def cube_fun(n_inp):
    result = []
    a_level = int(n_inp**(1/3))
    for a in range(a_level, -1, -1):
        b_inp = n_inp - a ** 3
        b_level = int(b_inp**(1/3))
        # print(b_inp, 'step a')
        if b_inp == 0:
            result.append(a)
            break
        # loop 1

        for b in range(b_level, -1, -1):
            c_inp = b_inp - b ** 3
            c_level = int(c_inp**(1/3))
            # print(c_inp, 'step b')
            if c_inp == 0:
                result.append(b)
                break
                # loop 2

            for c in range(c_level, -1, -1):
                d_inp = c_inp - c ** 3
                d_level = int(d_inp**(1/3))
                # print(d_inp, 'step c')
                if d_inp == 0:
                    result.append(c)
                    break
                    # loop 3
                for d in range(d_level, -1, -1):
                    e_inp = d_inp - d ** 3
                    e_level = int(e_inp**(1/3))
                    # print(e_inp, 'step d')
                    if e_inp == 0:
                        result.append(d)
                        break
                        # loop 4
                    for e in range(e_level, -1, -1):
                        f_inp = e_inp - e ** 3
                        f_level = int(f_inp**(1/3))
                        # print(f_inp, 'step e')
                        if f_inp == 0:
                            result.append(e)
                            break
                        for f in range(f_level, -1, -1):
                            g_inp = f_inp - f ** 3
                            g_level = int(g_inp**(1/3))
                            # print(g_inp, 'step f')
                            if g_inp == 0:
                                result.append(f)
                                break
                            for g in range(g_level, 0, -1):
                                h_inp = g_inp - g ** 3
                                # print(h_inp, 'step g')
                                if h_inp == 0:
                                    result.append(g)
                                    break

                            if len(result) != 0:
                                result.append(f)
                                break
                        if len(result) != 0:
                            result.append(e)
                            break
                        # end loop 4
                    if len(result) != 0:
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
        return ([0])
    else:
        return (result)


def cuber(a):
    output = 0
    for values in a:
        output += values ** 3
    return output


def MinOfCubed(k):
    # If k is less than the 2 ^ 3
    if (k < 8):
        return k;

        # Initialize with the maximum
    # number of cubes required
    res = k;
    for i in range(1, k + 1):
        if ((i * i * i) > k):
            return res;
        res = min(res, MinOfCubed(k - (i * i * i)) + 1);
    return res;


# Driver code  print(MinOfCubed(num));

# print(cube_fun(114))
all_works = dict()
for i in range(1000):
    evalueate_res = cube_fun(i)
    print(evalueate_res)
    good_result = cuber(evalueate_res) == i
    print(good_result, 'resuls', cuber(evalueate_res), i)
    all_works[i] = good_result

print(all_works)

for k, v in all_works.items():
    if v == False:
        print(k, 'fail')
        # print(MinOfCubed(k))
        print(cube_fun(k))

print(cube_fun(15))
