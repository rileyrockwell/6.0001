def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand_copy = hand.copy()
    iteration = 0

    if word == '':
        return False

    if word in wordList:
        for letter in word:
            # if letter is in the keys of the 'hand_copy' dictionary and the value associated with
            # hand_copy[letter] is not 'empty' (i.e. > 0 s.t. there exists a remaining letter to use
            # in the word)
            if letter in hand_copy and hand_copy.get(letter) != 0:
                # account for the iteration
                iteration += 1
                hand_copy[letter] = hand_copy.get(letter) - 1

        # if each letter in word was afffiliated with a corresponding value in hand_copy and the 
        # value was greater than zero (i.e. hand_copy[letter] > 0), return True
        return iteration == len(word)
    
    # if each letter in word was not affiliated with a corresponding value in hand_copy or we 
    # 'ran out' of letters (i.e. hand_copy[letter] == 0), return False
    return False