# Problem Set 2, hangman.py
# Name: 
# Collaborators: Peter Domitrovich
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "/Users/rileyrockwell/GitHub/6.0001/ps2/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # determine if each letter in secret word is also in wordlist. if so, +1 to counter; else, +0 to counter.
    counter = 0
    for i in secret_word:
        if i in letters_guessed:
            counter += 1
        else:
            counter += 0

    # determine if length of secret_word is equal to length of counter. return the correct boolean.
    if len(secret_word) == counter:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    string_to_display = []
    for i in secret_word:
        if i in letters_guessed:
            # display the value of i in 'string_to_display'
            string_to_display.append(i)
        else:
            string_to_display.append(' _ ')
    return ''.join(string_to_display)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_not_guessed = [i for i in string.ascii_lowercase]
    for i in letters_guessed:
        for j in letters_not_guessed:
            if i == j:
                letters_not_guessed.remove(j)
    return ''.join(letters_not_guessed)
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    number_of_guesses = 0
    n = 6
    warnings = 3

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", str(len(secret_word)), "letters long.")

    while number_of_guesses < n:
        
        if is_word_guessed(secret_word, letters_guessed) == False:
            print("--------")
            print("You have", str(n - number_of_guesses), "guesses left.")
            print("Available letters:", ''.join(get_available_letters(letters_guessed)))
            

            # get user input
            user_guess = str(input("Please guess a letter: ").lower())

            if user_guess in string.ascii_lowercase:
               letters_guessed.append(user_guess)
            else:
               warnings -= 1
               print("Oops! That is not a valid letter. You have", str(warnings), "warnings left:",
                     get_guessed_word(secret_word, letters_guessed))
               if warnings == 0:
                  number_of_guesses -= 1
            
            
            # REDO
            if letters_guessed[-1] in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                number_of_guesses += 1
        else:
            print("Congratulations, you guessed the secret word:", secret_word)
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_without_spaces = my_word.replace(' ', '')

    collection = 0
    for i in range(len(my_word_without_spaces)):
      if my_word_without_spaces[i] == other_word[i]:
        collection += 1
      elif my_word_without_spaces[i] == '_':
        collection += 1
      elif my_word_without_spaces[i] == ' ':
        collection += 0

    if collection == len(my_word_without_spaces) == len(other_word):
      return True
    else:
      return False
    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # strip 'my_word' of all spaces
    my_word = my_word.replace(' ', '')

    # build list of words from 'wordlist' that match 'my_word' (including underscores)
    list_to_return = []
    for i in wordlist:
      if len(i) == len(my_word):
        index_counter = 0
        a = True
        for j in my_word:
          if j != '_':
            if j != i[index_counter]:
              a = False
              break
          index_counter += 1
        if a:
          list_to_return.append(i)

    return list_to_return


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      match the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")

    letters_guessed = []
    number_of_guesses = 0
    n = 6
    warnings = 3

    print("I am thinking of a word that is", str(len(secret_word)), "letters long.")

    while True:
        print("You have", str(n - number_of_guesses), "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        # prompt the user for input (including uppercase letters)
        user_guess = input("Please guess a letter: ").lower()

        # if user_guess is "*", display the list of possible matches
        if user_guess == "*":
            print("Showing all matches...")
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            continue

        # if user_guess is not a valid entry: incorporate warnings
        if not user_guess.isalpha():
            warnings -= 1
            if warnings == 0:
                print("You have 0 warnings left", get_guessed_word(secret_word, letters_guessed))
                number_of_guesses += 1
                warnings = 3
            else:
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            continue

        elif user_guess in letters_guessed:
            warnings -= 1
            if warnings == 0:
                print("Oops! You've already guessed that letter.",
                      "You have 0 warnings left so you lose one guess",
                      get_guessed_word(secret_word, letters_guessed))
                # REVIEW: DETERMINE IF THAT TERMINATES THE GAME (I.E., OUT OF GUESSES)
                number_of_guesses += 1
                if number_of_guesses == n:
                    print("You you ran out of guesses. The word was", secret_word, ".")
                    break
                warnings = 3
            else:
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))

        # if user_guess is a valid entry: append to 'letters_guessed' and
        # determine if user_input is in the secret_word
        letters_guessed.append(user_guess)
        if user_guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            number_of_guesses += 1

        if is_word_guessed(secret_word, letters_guessed):
            print("-------------")
            print("Congratulations, you won!")
            break
        # INCORPORATE SCORING
        elif not is_word_guessed(secret_word, letters_guessed) and number_of_guesses == n:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was", secret_word, ".")
            break
        # if the above 2 conditions are not met, cycle back through the while loop to prompt the user
        # for an additional guess


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # wordlist = load_words(), from line 51

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 


    # print(match_with_gaps('t_ _ ting', 'testing'))
    # print(match_with_gaps('testing', 'testing'))
    # print(match_with_gaps('testinx', 'testing'))
        
    # print(show_possible_matches('t_ _ t_ _ g')) #should generate x matches
    # print(show_possible_matches('t_ _ t_ ng'))  #should generate y matches, s.t. x > y
    # print(show_possible_matches('t_ _ ting'))   #should generate z matches, s.t. y > z
    # print(show_possible_matches('t_ sting'))


    secret_word = "testing"
    # secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    # print(match_with_gaps("t_ _ ting", "testing")) # should return True.
    # print(match_with_gaps("testing", "testing")) # should return True.
