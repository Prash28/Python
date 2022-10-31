import random
import string

words=[]

file = open('words.txt')
for word in file:
    word = word[:-1]
    words.append(word)

# print(words)

def get_valid_word(words):
    word1 = random.choice(words)
    while '-' in word1 or ' ' in word1:
        word1 = random.choice(words)
    return word1
def hangman():

    hangman_pics = ['''
    +---+
         |
         |
         |
        ===''','''
    +---+
    O   |
        |
        |
       ===''','''
    +---+
    O   |
    |   |
        |
       ===''','''
    +---+
    O   |
   /|   |
        |
       ===''','''
    +---+
    O   |
   /|\  |
        |
       ===''','''
    +---+
    O   |
   /|\  |
   /    |
       ===''','''
    +---+
    O   |
   /|\  |
   / \  |
       ==='''
    ]
    lives=7
    alphabet = set(string.ascii_uppercase)
    # print(alphabet)
    #print(len(alphabet)) --prints out 26
    word = get_valid_word(words).upper()
    print("The computer has chosen a word")
    # print(word)
    letters_in_word = set(word)
    # print(letters_in_word)
    used_letters = set()

    while len(letters_in_word) > 0:
        print("You have used these letters: ",' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("current_word: ",' '.join(word_list))
        # print(word_list)
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters_in_word:
                letters_in_word.remove(user_letter)
            else:
                print(hangman_pics[abs(lives-7)])
                lives -= 1
                print(f"Lives left: {lives}")
                if(lives == 0):
                    print("GAME OVER!")
                    print(f"The word is {word}")
                    break
        elif user_letter in used_letters:
            print("You have already used this letter. Please try another letter")
        else:
            print("Enter a valid letter!")
    
    print(f"Congrats!! You have guessed the word {word} correctly!")

while(True):
    print("Welcome to HANGMAN :)")
    hangman()
    reply=input("Want to play another game(Y/N)?")
    if(reply.upper() == 'N'):
        print("Thank you for playing! Good bye")
        break
    else:
        continue
            