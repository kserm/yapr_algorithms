# 70304052
from typing import List


def find_nearest_empty(empty_list: List,
                       distance: int) -> List:
    result_list: List = [0] * distance
    prev_zero: int = 0
    for zero in empty_list:
        if zero == empty_list[0] and zero != 0:
            for i in range(zero):
                result_list[i] = zero - i
        elif zero <= distance:
            for i in range(prev_zero, zero):
                result_list[i] = min(i - prev_zero, zero - i)
        prev_zero = zero
    if empty_list[-1] < distance - 1:
        for i in range(empty_list[-1], distance):
            result_list[i] = i - empty_list[-1]
    return result_list


if __name__ == '__main__':
    n: int = int(input())
    house_list: List = [int(i) for i in input().split()]
    distance: int = len(house_list)
    zero_list: List = [i for i in range(distance) if house_list[i] == 0]
    print(*find_nearest_empty(zero_list, distance), end=' ')
