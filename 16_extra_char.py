str1 = input()
str2 = input()


def find_extra_char(string1, string2):
    temp_str_long = []
    temp_str_short = []
    if len(string1) >= len(string2):
        temp_str_long = list(string1)
        temp_str_short = list(string2)
    else:
        temp_str_long = list(string2)
        temp_str_short = list(string1)

    for char in temp_str_short:
        if char in temp_str_long:
            temp_str_long.pop(temp_str_long.index(char))

    return temp_str_long[0]


print(find_extra_char(str1, str2))
