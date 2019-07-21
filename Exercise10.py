
'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(numbers):
    score = 1
    for i in numbers:
        if i % 2 == 0:
            score = score * i
    return score

print(multiply_even_numbers())



