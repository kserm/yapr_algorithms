def zip_arr(arr1, arr2):
    res = (zip(arr1, arr2))
    for t in res:
        for i in t:
            print(i, end=' ')


if __name__ == '__main__':
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    zip_arr(arr1, arr2)
