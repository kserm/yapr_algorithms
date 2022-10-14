def twosum(n, k):
    for i in range(0, len(n)):
        for j in range(i+1, len(n)):
            if n[i] + n[j] == k:
                return n[i], n[j]
    return None


if __name__ == '__main__':
    n_chips = int(input())
    chips_list = [int(i) for i in input().split()]
    k = int(input())
    res = twosum(chips_list, k)
    if res:
        print(*res, end=' ')
    else:
        print(res)
