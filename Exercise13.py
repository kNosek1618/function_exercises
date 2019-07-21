


def intersection(list1, list2):
    same = []
    for i in list1:
        for e in list2:
            if i == e:
                same.extend([i])
    return same


print(intersection([1, 2, 3], [2, 3, 4]))







# a = [1, 2, 3]
# b = [2, 3, 4]
# same = []
#
#
# for i in a:
#     for e in b:
#         if i == e:
#             same.extend([i])
#
# print(same)


