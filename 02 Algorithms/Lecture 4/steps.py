steps = int(input())


def options(n):

    step_options = [0 for i in range(max(n, 3))]
    step_options[0] = 1
    step_options[1] = 1
    step_options[2] = 2

    if n < 3:
        return step_options[n]

    for i in range(3, n):
        step_options[i] = step_options[i - 1] + step_options[i - 2] + step_options[i - 3]
    return step_options[-1]


print(options(steps+1))
