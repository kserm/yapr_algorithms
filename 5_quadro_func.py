def quadro_func(a, x, b, c):
    y = a*x*x + b*x + c
    return y


if __name__ == '__main__':
    a, x, b, c = [int(i) for i in input().split()]
    print(quadro_func(a, x, b, c))
