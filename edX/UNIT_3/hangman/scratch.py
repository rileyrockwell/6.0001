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

