import itertools

n_inp = int(input())


def cube_dict_create(int_input):
    cube_dict = {}
    for i in range(0, int(int_input ** (1 / 3)) + 1):
        #         print(i, i**3)
        cube_dict[i] = i ** 3
    return cube_dict


def cuber_v2(value_given):
    result = []
    a = cube_dict_create(value_given)
    for i in itertools.combinations_with_replacement(a.keys(), 7):
        sum_el = 0
        for temp_val in i:
            sum_el += a[temp_val]
        if sum_el == value_given:
            result = i
            break
    if len(result) == 0:
        return [0]
    else:
        result = [a[i] for i in result if i != 0]
        return result


print(*cuber_v2(n_inp))
