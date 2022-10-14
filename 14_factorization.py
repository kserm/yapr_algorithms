number = 917521579


# number = int(input())

def factorization(num):
    result = []
    temp_num = num
    divider = 2
    while temp_num > 1:
        if temp_num % divider == 0:
            temp_num = temp_num / divider
            result.append(divider)
        else:
            if divider * divider < temp_num:
                divider += 1
            else:
                divider = int(temp_num)
    return result

for i in factorization(number):
    print(i, end=' ')