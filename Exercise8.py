
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(word):
    word = word.replace(' ', '')
    word = word.upper()
    x = len(word)
    drow = ''
    for l in word:
        x -= 1
        drow += word[x]
        if word == drow:
            return True
    return False

print(is_palindrome('a man a plan a canal Panama')) # True

##########################################################
# More shorter explain !

def is_palindrome(string):
    return string == string[::-1]

###################################

# word = 'abcde'
# x = len(word)
# drow = ''
#
# for l in word:
#     x -= 1
#     drow += word[x]
#     print(word[x])
#
# print(drow)

################################
# DELETING ALL WHITE SPACES
# x = 'kobyla ma maly bok'
# x= x.replace(" ", '')
# print(x)

