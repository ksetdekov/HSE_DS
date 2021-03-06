import itertools
def cube_split(n_inp):
    import math
    # n_inp = int(input())
    result = []

    def c_root(k):
        """cube root calculator based on newton formula"""
        start = math.floor(len(str(k).encode('utf-8')) / 3) + 1
        x = start
        while True:
            x = (x - (x ** 3 - k) / (3 * x ** 2)) // 1
            if x ** 3 <= k < (x + 1) ** 3:
                break
        return int(x)

    a_level = c_root(n_inp)
    for a in range(a_level+1):
        b_inp = n_inp - a ** 3
        b_level = c_root(b_inp)
        # print(b_inp, 'step a')
        if b_inp == 0:
            result.append(a)
            break
        # loop 1

        for b in range(b_level+1):
            c_inp = b_inp - b ** 3
            c_level = c_root(c_inp)
            # print(c_inp, 'step b')
            if c_inp == 0:
                result.append(b)
                break
                # loop 2

            for c in range(c_level+1):
                d_inp = c_inp - c ** 3
                d_level = c_root(d_inp)
                # print(d_inp, 'step c')
                if d_inp == 0:
                    result.append(c)
                    break
                    # loop 3
                for d in range(d_level+1):
                    e_inp = d_inp - d ** 3
                    e_level = c_root(e_inp)
                    # print(e_inp, 'step d')
                    if e_inp == 0:
                        result.append(d)
                        break
                        # loop 4
                    for e in range(e_level+1):
                        f_inp = e_inp - e ** 3
                        f_level = c_root(f_inp)
                        # print(f_inp, 'step e')
                        if f_inp == 0:
                            result.append(e)
                            break
                        for f in range(f_level+1):
                            g_inp = f_inp - f ** 3
                            g_level = c_root(g_inp)
                            # print(g_inp, 'step f')
                            if g_inp == 0:
                                result.append(f)
                                break
                            for g in range(g_level+1):
                                h_inp = g_inp - g ** 3
                                h_level = c_root(h_inp)
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
        return ('0')
    else:
        return(result)


results = {}
a = itertools.combinations_with_replacement([0, 1, 2, 3, 4], 7)
for i in a:
    sum = 0
    for m in i:
        sum += m**3
    results[sum] = i
all_works = []
for k,v in results.items():
    list_result = cube_split(k)

    sum_res = 0
    for m in list_result:
        sum_res += m**3
    matches = k == sum_res
    all_works.append(matches)
    print(matches, k, 'input' , sum_res, 'my alg')

print(all(all_works))
