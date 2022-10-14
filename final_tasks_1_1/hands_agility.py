# 70303427
from typing import List


def count_score(k: int, arr: List) -> int:
    score: int = 0
    for t in range(1, 10):
        digit_sum: int = 0
        for item in arr:
            for digit in item:
                if digit == str(t) and digit != '.':
                    digit_sum += 1
        if digit_sum != 0:
            if digit_sum <= k*2:
                score += 1
    return score


if __name__ == '__main__':
    k: int = int(input())
    m: List = []
    for i in range(4):
        m += list(input().split())
    print(count_score(k, m))
