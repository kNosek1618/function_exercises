
'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(values):
    compact = []
    for i in values:
        if i != False and i != None and i != '' and i != [] and i != {}:
            compact.append(i)
    return compact

print(compact())


