# from collections import Counter
#
#
# def count_words(words):
#     return Counter(words)
#
#
# my_string = "Hello World"
#
# print(count_words(my_string))

def count_words(words):
    char_count = {}
    for word in words:
        if word in char_count:
            char_count[word] += 1
        else:
            char_count[word] = 1
    return char_count


my_string = "hello world"
print(count_words(my_string))
