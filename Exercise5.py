

def single_letter_count(word, letter):
    '''
    single_letter_count("Hello World", "h") # 1
    single_letter_count("Hello World", "z") # 0
    single_letter_count("HelLo World", "l") # 3
    '''
    count = 0
    for l in word:
        if l == letter:
            count += 1
    return count

print(single_letter_count())



##################################

# x = 'draw'
# print(len(x)) # 4

# word = "Hello"
# count = len(word)
#
# while count > 0:
#     count -= 1
#     print(count)

###############################

# word = "hello"
# list = []
#
# for l in word:
#     print(l)
