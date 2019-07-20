

def multiple_letter_count(word):
    '''
    multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
    '''
    dict = {}
    for l in word:
        key = (l)
        value = (word.count(l))
        dict[key] = value
    return dict

print(multiple_letter_count('awesome'))

# # # RESULT # # #
# {'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1}

##############################################################




# def single_letter_count(word, letter):
#     count = 0
#     for l in word:
#         if l == letter:
#             count += 1
#     return count
#################################

# word = 'awesome'
# dict = {}
#
# for l in word:
#     key = (l)
#     value = (word.count(l))
#     dict[key] = value
#
# print(dict)

#################################
# word = "amazing"
# index = 1
#
# for letter in alphabet:
#     if letter == word[index]:
#         print(letter)


