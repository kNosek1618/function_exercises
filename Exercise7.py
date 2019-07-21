
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(param1,param2,param3,param4=None):
    if param2 == 'remove':
        if param3 == 'end':
            remove = param1.pop()
            return remove
        elif param3 == 'beginning':
            remove = param1.pop(0)
            return remove
    elif param2 == 'add':
        if param3 == 'beginning':
            param1.insert(0, param4)
            return param1
        elif param3 == 'end':
            param1.extend([param4])
            return param1


print(list_manipulation())


# list = [1, 2, 3]
# print(list)


