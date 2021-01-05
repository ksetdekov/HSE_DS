a = int(input())

def fib_last(n):
    if n <= 2:
        return 1

    else:
        prev, prev_prev = (1, 1)
        for _ in range(2, n):
            current = (prev + prev_prev)%10
            prev_prev = prev
            prev = current

        return current

print(fib_last(a))
