cur_inp = int(1)
squares = ''


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


def is_square(k):
    if k < 0:
        raise ValueError("works on non-negative")
    elif integer_sqrt(k) ** 2 == k:
        return True
    else:
        return False


def t_reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


while True:
    cur_inp = int(input())
    if cur_inp == 0:
        break
    if is_square(cur_inp):
        squares = squares + ' ' + str(cur_inp)
if squares == '':
    print(str(0))
else:
    result = tuple(squares.split())
    result = t_reverse(result)
    print(' '.join(result))
