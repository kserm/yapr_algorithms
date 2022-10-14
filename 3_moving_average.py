def moving_average(timeseries, K):
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)
    for i in range(0, len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result


if __name__ == '__main__':
    n_sec = int(input())
    timeseries = [int(i) for i in input().split()]
    k = int(input())   
    res = moving_average(timeseries, k)
    print(*res, end=' ')
