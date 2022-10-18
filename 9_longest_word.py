chars_num = int(input())
words_str = input()


def find_longest_word(some_text):
    longest_word = ''
    words_list = list(some_text.strip().split())
    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


print(find_longest_word(words_str))
print(len(find_longest_word(words_str)))
