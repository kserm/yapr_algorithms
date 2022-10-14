def twosum_v2(n, k):
    n.sort()
    i = 0
    j = len(n)-1
    while i < j:
        if n[i] + n[j] == k:
            return n[i], n[j]
        elif n[i] + n[j] > k:
            j -= 1
        elif n[i] + n[j] < k:
            i += 1
    return None


def twosum_v3(n, k):
    previus = set()
    for a in n:
        y = k - a
        if y in previus:
            return a, y
        else:
            previus.add(a)
    return None


if __name__ == '__main__':
    n_chips = int(input())
    chips_list = [int(i) for i in input().split()]
    k = int(input())
    res = twosum_v3(chips_list, k)
    if res:
        print(*res, end=' ')
    else:
        print(res)
