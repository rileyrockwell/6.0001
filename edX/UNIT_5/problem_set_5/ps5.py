import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    # print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = '/home/riley/6.0001/edX/UNIT_5/problem_set_5/words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that maps each letter (both uppercase and lowercase) to a shifted letter.
        
        shift (integer): the amount by which to shift each letter.
        
        Returns: A dictionary mapping a letter to another letter after applying the shift.
        '''
        shift_dict = {}
        lowercase_letters = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
        uppercase_letters = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # Shift lowercase letters
        for i in range(len(lowercase_letters)):
            shifted_index = (i + shift) % 26
            shift_dict[lowercase_letters[i]] = lowercase_letters[shifted_index]
        
        # Shift uppercase letters
        for i in range(len(uppercase_letters)):
            shifted_index = (i + shift) % 26
            shift_dict[uppercase_letters[i]] = uppercase_letters[shifted_index]

        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift.
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)  # Get the shift dictionary
        encrypted_message = ''

        # Iterate through each character in the message
        for char in self.message_text:
            if char in shift_dict:
                encrypted_message += shift_dict[char]  # Shift the letter
            else:
                encrypted_message += char  # Keep non-letter characters unchanged

        return encrypted_message
        
    def build_shift_dict1(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        initial_dict = {key: value for value, key in enumerate(string.ascii_letters)}

        reference_dict = {key: value for key, value in enumerate(string.ascii_letters)}

        return_dict = {key: reference_dict[(initial_dict[key] + shift) % 52] for key in initial_dict}

        return return_dict


    def apply_shift1(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
            
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
                 down the alphabet by the input shift
        '''
        return_message_text = ''
        
        # Ensure that shift is within the valid range
        shift = shift % 26

        for char in self.message_text:
            # if character is a letter (i.e. not a space or punctuation), apply the shift
            if char in string.ascii_letters:
                return_message_text += self.build_shift_dict(shift)[char]
            # if character is not a letter (i.e. is a space or punctuation)
            else:
                return_message_text += char

        return return_message_text


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        if not (0 <= shift < 26):
            raise ValueError('0 <= shift < 26')

        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)


    def decrypt_message1(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        evaluation_dict = {}

        # test different shift values
        for shift_value in range(26):
            # something
            shifted_message = self.apply_shift(shift_value)
            
            # start somewhere
            shifted_message = shifted_message.split()
            valid_word_count = 0

            for word in shifted_message:
                if word in self.valid_words:
                    valid_word_count += 1

            # create a dictioanry mapping the shift value to the valid_word_count
            evaluation_dict[shift_value] = valid_word_count

        return evaluation_dict.values()


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        max_valid_words = 0
        best_shift = 0
        best_decrypted_message = ""
        
        # Test all possible shifts
        for shift in range(26):
            decrypted_message = self.apply_shift(shift)
            word_list = decrypted_message.split()
            valid_word_count = sum([is_word(self.valid_words, word) for word in word_list])
            
            # Check if this shift gives more valid words
            if valid_word_count > max_valid_words:
                max_valid_words = valid_word_count
                best_shift = shift
                best_decrypted_message = decrypted_message
        
        return best_shift, best_decrypted_message



#Example test case (PlaintextMessage)
# plaintext = PlaintextMessage('hello', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.get_message_text_encrypted())
    
# #Example test case (CiphertextMessage)
# ciphertext = CiphertextMessage('jgnnq')
# print('Expected Output:', (24, 'hello'))
# print('Actual Output:', ciphertext.decrypt_message())

instance = CiphertextMessage('testing message text')
testing_str = instance.apply_shift(1)
print(testing_str)
instance = CiphertextMessage(testing_str)
print(instance.apply_shift(25))
print(instance.decrypt_message())

story = get_story_string()
instance = CiphertextMessage(story)
print(instance.decrypt_message())