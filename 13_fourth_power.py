digit = int(input())


def is_fourth_power(num):
    temp_num = num
    flag = False
    if num == 1:
        flag = True
    else:
        while temp_num >= 4:
            rem = temp_num % 4
            if rem == 0:
                temp_num = temp_num / 4
                if temp_num == 1:
                    flag = True
                else:
                    flag = False
            else:
                return False
    return flag


print(is_fourth_power(digit))
