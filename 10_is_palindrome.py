words_str = 'A man, a plan, a canal: Panama'

words_str = input()

EXCLUDED_CHARS = [' ', ':', ',', '.', '!', '?', '-', ';']


def format_string(input_str):
    formated_str = input_str.strip().lower()
    chars_list = []
    for char in formated_str:
        if char in EXCLUDED_CHARS:
            continue
        else:
            chars_list.append(char)
    return ''.join(chars_list)


def is_palindrome(arg):
    if list(arg) == list(reversed(arg)):
        return True
    else:
        return False


print(is_palindrome(format_string(words_str)))
