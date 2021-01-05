N = int(input())


def calc(n):
    steps = [0 for _ in range(n)]
    steps[0] = 0
    # print(steps)
    for i in range(1, n):
        value = i + 1
        # print(value, 'value')

        if value % 3 == 0:
            # print('div 3')
            if value % 2 == 0:
                steps[i] = min(steps[(value // 3 - 1)]+1, steps[(value // 2 - 1)]+1)
            else:
                steps[i] = steps[(value // 3 - 1)] + 1
        elif value % 2 == 0:
            # print('div 2')

            steps[i] = steps[(value // 2 - 1)] + 1
        else:
            steps[i] = steps[i - 1] + 1
    # print(steps)

    return steps[-1]


print(calc(N))
