def odd_even_contest(a, b, c):
    a_rem = a % 2
    b_rem = b % 2
    c_rem = c % 2
    if (a_rem == 0 and b_rem == 0 and c_rem == 0):
        return 'WIN'
    elif (a_rem != 0 and b_rem != 0 and c_rem != 0):
        return 'WIN'
    else:
        return 'FAIL'


if __name__ == '__main__':
    a, b, c = [int(i) for i in input().split()]
    print(odd_even_contest(a, b, c))
