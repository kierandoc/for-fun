import random
import string 
from words import words  #importing variable from other .py file containing all the words i'll use.


def get_valid_word(words):
    word = random.choice(words) #randomly choses something from the list.
    while '-' in word or ' ' in word:
        word = random.choice(words)


    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #_list letters in word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()  #what the user has guessed


    while len(word_letters) > 0:
        #letters used       
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have already used the letter:", " ".join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:" + " ".join(word_list))



        user_letters = input('Guess a letter :').lower()


        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters :
                word_letters.remove(user_letters)
                
        
        elif user_letters in used_letters:
            print("You already guessed that letter. Try again.")

        else: 
            print("Invalid character.")

 
hangman()
