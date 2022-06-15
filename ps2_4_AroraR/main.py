"""
Description: this function uses recursion to write a function for determining if a string s has more vowels than consonants.
Date Created/Last Modified: 11/8
Original Author: Rahul Arora
"""

#creating function to run count function with default parameters; this prevents the user from needing to enter the default parameters for letter_num, vowels, and consonants
def run_count(input_word):
    #running count with default, first values (0,0,0)
    return count(input_word, 0, 0, 0)


def count(word, letter_num, vowels, consonants):
    #base case
    if(letter_num == len(word) ):
        #evaluate results, see if vowels > consonants
        if(vowels > consonants):
            return True
        else:
            return False

    #checking to see if the current letter is a vowel
    if(word[letter_num] == 'a'   or  word[letter_num] == 'e'  or word[letter_num] == 'i'   or word[letter_num] == 'o'  or word[letter_num] == 'u'):
        # if current letter is a vowel, recursively go through next iteration with vowels + 1
        return count(word, letter_num+1, vowels+1, consonants)
    else:
         # if current letter is not a vowel,recursively go through next iteration with consonants + 1
     return count(word, letter_num+1, vowels, consonants+1)


#testing
print(run_count("aeiou"))
print(run_count("rstlne"))
print(run_count("Hello"))
print(run_count("abcdefghijklmnopqrstuvwxyz"))
print(run_count("abe"))
print(run_count("test"))
print(run_count("banana"))
print(run_count("baanana"))


