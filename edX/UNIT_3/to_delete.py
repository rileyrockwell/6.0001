        # if the user selects a letter they have already selected in a prior round
        if guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
            guessesRemaining -= 1


        # if the user selects a letter that is not in secret word
        elif guess not in secretWord:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            guessesRemaining -= 1
            lettersGuessed.append(guess)

        # if the user selects a letter that is in secret word
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            guessesRemaining -= 1

        # ensure the user has guesses remaining
        if guessesRemaining == 0:
            print('-----------')
            print('Sorry, you ran out of guesses. The word was', secretWord + '.')
            break

    if isWordGuessed(secretWord, lettersGuessed):
        print('-----------')
        print('Congratulations, you won!')


###

# FILL IN YOUR CODE HERE...

    lettersGuessed = []
    mistakesMade = 0
    guessesRemaining = 8
    substring = ''


    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    
    # while the word is not guessed
    while isWordGuessed(secretWord, lettersGuessed) == False:
        print('-------------')
        print('You have', guessesRemaining, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = str(input('Please guess a letter: '))
        
        if guessesRemaining <= 1:
            print('Sorry! That is not in the word. The word was:', secretWord)
            break

        ###
        # if guess is in 'secretWord' and has not been guessed
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            # do not change guessesRemaining

        # if guess not in 'secretWord' and has not been guessed
        elif guess not in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in the word.', getGuessedWord(secretWord, lettersGuessed))
            guessesRemaining -= 1

        elif guess in secretWord and guess in lettersGuessed:
            # do not change lettersGuessed
            print('Oops! You already guessed that letter (in the word).', getGuessedWord(secretWord, lettersGuessed))
            guessesRemaining -= 1
        
        elif guess not in secretWord and guess in lettersGuessed:
            print('Oops! You already guessed that letter (not in the word).', getGuessedWord(secretWord, lettersGuessed))
            guessesRemaining -= 1

    if isWordGuessed(secretWord, lettersGuessed) == True:
      print('Congratulations, you won!', getGuessedWord(secretWord, lettersGuessed))

        
                
                



# secretWord = chooseWord(wordlist).lower()
secretWord = chooseWord(wordlist)
hangman('testing')