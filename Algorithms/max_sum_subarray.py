def max_sum_subarray(array):
    """выдает длину и сумму подстроки, которая дает максимальную сумму
    на массиве np.random.rand(1000)-0.5) работает в 37 раз быстрее,
    чем алогиртм с лекции """

    n = len(array)
    # all prefix sum compute
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + array[i])
    start, finish, start_last, finish_last = 0, 0, -1, -1
    start_old = -1
    finish_old = -1

    ans = -1
    max_sum = -float("inf")
    while start != n - 1:
        # критерий остановки - дошли до предпоследнего места указателем начала
        if finish == n or ((finish == finish_old) and (start == start_old)):
            # если дошли указателем конца или два раза смотрим то же место - двигать начало
            start += 1
            current_sum = prefix_sum[finish + 1] - prefix_sum[start]
            if current_sum > max_sum:
                max_sum, ans = current_sum, finish - start + 1

        try:
            # если доходим до конца, следующего движения уже нет, поэтому, следующая сумма даст IndexError,
            # переставляю индикатор движения вперед по более большой сумме на False
            sum_check = (prefix_sum[finish] - prefix_sum[start + 1]) < (prefix_sum[finish + 2] - prefix_sum[start])
        except IndexError:
            sum_check = False
        if ((finish - start) < 1 or sum_check) and (finish + 2 < len(prefix_sum)):
            finish += 1
            current_sum = prefix_sum[finish + 1] - prefix_sum[start]
            if current_sum > max_sum:
                max_sum, ans = current_sum, finish - start + 1
        start_old = start_last
        start_last = start
        finish_old = finish_last
        finish_last = finish

    return ans, max_sum


X = [1, 2, -4, 5, 2, -1, 3, -10, 7, 1, -1, 2]

print(max_sum_subarray(X))
