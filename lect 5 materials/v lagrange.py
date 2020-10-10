n_inp = 1000
result = []


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


a_level = integer_sqrt(n_inp)
for a in range(a_level, 0, -1):
    b_inp = n_inp - a ** 2
    b_level = integer_sqrt(b_inp)
    print(a, 'step a')
    if b_inp == 0:
        result.append(a)
        break
    # loop 1

    for b in range(b_level, 0, -1):
        c_inp = b_inp - b ** 2
        c_level = integer_sqrt(c_inp)
        print(c_inp, 'step b')
        if c_inp == 0:
            result.append(b)
            break
            # loop 2

        for c in range(c_level, 0, -1):
            d_inp = c_inp - c ** 2
            d_level = integer_sqrt(d_inp)
            print(d_inp, 'step d')
            if d_inp == 0:
                result.append(c)
                break
                # loop 3
            for d in range(d_level, 0, -1):
                e_inp = d_inp - d ** 2
                print(e_inp, 'step e')
                if e_inp == 0:
                    result.append(d)
                    break

                # end loop 3
            if len(result) != 0:
                result.append(c)

            # end loop 2
        if len(result) != 0:
            result.append(b)
            break

    # end loop 1
    if len(result) != 0:
        result.append(a)
        break

print(*result, "output")
