def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return_tup = ()
    for item in range(len(aTup)):
        print(aTup[item])
        if item % 2 == 0:
            return_tup += (aTup[item],)
            
    return return_tup

def oddTuples(aTup):
    return aTup[::2]


print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))