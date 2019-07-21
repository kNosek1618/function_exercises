
'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def isEven(num):
    return num % 2 == 0


def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

print(partition([1, 2, 3, 4], isEven()))








# list = [1, 2, 3, 4]
# even = []
# odd = []
#
# for i in list:
#     if isEven(i):
#         even.extend([i])
#     else:
#         odd.extend([i])
#
# print(even)
# print(odd)