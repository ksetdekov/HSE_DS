N = int(input())
stairs = list(map(int, input().split()))


def pay_stair(prices, counts):
    step_back = 0
    two_steps_back = 0
    for i in range(counts):
        costs = min(step_back, two_steps_back) + prices[i]
        two_steps_back = step_back
        step_back = costs

    return costs


print(pay_stair(stairs, N))
