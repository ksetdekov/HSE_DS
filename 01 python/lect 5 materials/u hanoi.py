n_inp = int(input())

n = [i for i in range(1, n_inp + 1)]


def move(n, x=1, y=3):
    """ hanoi mover которая печатает последовательнось перекладываний дисков для перемещения пирамидки высоты n со
    стержня номер x """
    mid = 6 - x - y

    if len(n) == 1:
        print(n[0], x, y)
    else:
        move(n[:len(n) - 1], x=x, y=mid)
        move(n[len(n) - 1:], x=x, y=y)
        move(n[:len(n) - 1], x=mid, y=y)


move(n)
