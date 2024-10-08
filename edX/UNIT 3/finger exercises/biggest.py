def biggest(aDict):
	new_dict = {}
	for key, value in aDict.items():
		new_dict[key] = len(aDict[key])

	return max(new_dict, key=new_dict.get)


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))