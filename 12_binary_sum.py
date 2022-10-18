digit1 = int(input())
digit2 = int(input())


def binary_sum(num1, num2):
    res_list = []
    carry = 0
    rng_max = 0
    rng_min = 0
    num1_list = list(map(int, list(str(num1))))
    num2_list = list(map(int, list(str(num2))))
    rng1 = len(num1_list)
    rng2 = len(num2_list)
    if rng1 > rng2:
        rng_max = rng1
        rng_min = rng2
    else:
        rng_max = rng2
        rng_min = rng1
    if rng_max > 0:
        for i in range(1, rng_min+1):
            if num2_list[-i] == 1 and num1_list[-i] == 1 and carry == 0:
                carry = 1
                res_list.append(0)
            elif num2_list[-i] == 1 and num1_list[-i] == 1 and carry == 1:
                carry = 1
                res_list.append(1)
            elif num2_list[-i] == 0 and num1_list[-i] == 0:
                if carry == 1:
                    res_list.append(1)
                    carry = 0
                else:
                    res_list.append(0)
            else:
                if carry == 1:
                    res_list.append(0)
                    carry = 1
                else:
                    res_list.append(1)

        if rng1 > rng2:
            for i in range(rng_min+1, rng_max+1):

                if carry == 1:
                    if num1_list[-i] == 1:
                        res_list.append(0)
                        carry = 1
                    else:
                        res_list.append(1)
                        carry = 0
                else:
                    res_list.append(num1_list[-i])
        else:
            for i in range(rng_min+1, rng_max+1):
                if carry == 1:
                    if num2_list[-i] == 1:
                        res_list.append(0)
                        carry = 1
                    else:
                        res_list.append(1)
                        carry = 0
                else:
                    res_list.append(num2_list[-i])
    else:
        res_list.append(0)
    if carry == 1:
        res_list.append(1)
    return ''.join(map(str, list(reversed(res_list))))


print(binary_sum(digit1, digit2))
