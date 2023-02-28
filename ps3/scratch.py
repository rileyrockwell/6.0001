    sum_of_letter_values = 0
    for i in word.lower():
        # obtain the value of the key:value pair from the SCRABBLE_LETTERS_DICTIONARY
        sum_of_letter_values += SCRABBLE_LETTER_VALUES[i]

    abstract_sum = 7 * len(word) - 3 * (n - len(word))
    if abstract_sum > 1:
        abstract_sum = abstract_sum
    else:
        abstract_sum = 1

    return sum_of_letter_values * abstract_sum


# print(get_word_score('aaa', 3))

print(1)