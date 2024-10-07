def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # does not modify hand (i.e. does not mutate the original dictionary)
    new_hand = hand.copy()

    # evaluate each letter in 'word' in order to reduce its value by 1 in the 
    # new_hand dictionary (given the letter exists)
    for letter in word:
        # if the letter key (new_dict[letter]) has a value that is not empty (i.e.
        # equal to zero)
        if new_hand.get(letter, 0) != 0:
            # reduce the integer value in the key:value pair by a value of 1.
            new_hand[letter] -= 1

    return new_hand





