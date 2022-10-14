digit = 156
digit = int(input())

def decimal_to_binary(number):
    bin_list = []
    temp_num = number
    if number == 0:
        bin_list.append(0)
    else:
        while temp_num >= 1:
            bin_list.append(temp_num % 2)
            temp_num = temp_num // 2
    return ''.join(map(str, list(reversed(bin_list))))

print(decimal_to_binary(digit))