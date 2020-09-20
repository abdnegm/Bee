"""
Parses .txt files of level 1, 2, and 3 spelling bee
words (where words separated by spaces or new lines)
into .pickle files.
"""

import pickle

#File locations of difficulties
LEVEL_ONE_PATH = 'Words_of_the_Champions_Printable_1.txt'
LEVEL_TWO_PATH = 'Words_of_the_Champions_Printable_2.txt'
LEVEL_THREE_PATH = 'Words_of_the_Champions_Printable_3.txt'

def get_words(path):
    words = []
    with open(path) as f:
        for line in f:
            if line != '':
                words.extend(line.split())
    return words

def picklee(obj, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(obj, f)
    return

if __name__ == "__main__":
    level_one_words = get_words(LEVEL_ONE_PATH)
    level_two_words = get_words(LEVEL_TWO_PATH)
    level_three_words = get_words(LEVEL_THREE_PATH)
    
    picklee(level_one_words, 'level_one_words.pickle')
    picklee(level_two_words, 'level_two_words.pickle')
    picklee(level_three_words, 'level_three_words.pickle')
