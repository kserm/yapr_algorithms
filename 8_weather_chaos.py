def weather_chaos(numbers):
    chaos = 0
    rng = len(numbers)
    if rng > 1:
        for i in range(1, rng-1):
            if numbers[i-1] < numbers[i] > numbers[i+1]:
                chaos += 1
        if numbers[0] > numbers[1]:
            chaos += 1
        if numbers[-1] > numbers[-2]:
            chaos += 1
    else:
        chaos += 1
    return chaos


if __name__ == '__main__':
    days = int(input())
    weather_list = [int(i) for i in input().split()]
    print(weather_chaos(weather_list))
