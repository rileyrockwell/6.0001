def how_many(aDict):
    values = aDict.values()
    total_sum = 0
    for value in values:
        total_sum += len(value)

    return total_sum
    


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))