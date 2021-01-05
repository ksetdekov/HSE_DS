a = float(input())
b = float(input())
c = float(input())
d = float(input())


def distance(x1, x2, x3, x4):
    return ((x1 - x3) ** 2 + (x2 - x4) ** 2) ** 0.5


print(f'{distance(a, b, c, d):.5f}')
