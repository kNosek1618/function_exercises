



def return_day(day):
    '''
    Program returning day according number
    return_day(1) # "Sunday"
    return_day(2) # "Monday"
    return_day(3) # "Tuesday"
    return_day(4) # "Wednesday"
    return_day(5) # "Thursday"
    return_day(6) # "Friday"
    return_day(7) # "Saturday"
    return_day(41) # None
    '''
    dict = {1:'Sunday',
            2:'Monday',
            3:'Tuesday',
            4:'Wednesday',
            5:'Thursday',
            6:'Friday',
            7:'Saturday'}
    if day == 1:
        return dict[day]
    elif day == 2:
        return dict[day]
    elif day == 3:
        return dict[day]
    elif day == 4:
        return dict[day]
    elif day == 5:
        return dict[day]
    elif day == 6:
        return dict[day]
    elif day == 7:
        return dict[day]
    pass

print(return_day(8))
print(return_day.__doc__)