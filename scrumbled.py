import random

words=["mangoes","earth","mother","family","mismatched"]

def jumble_word(word):
    return "".join(random.sample(word,len(word)))

def play_game():
    word=random.choice(words)
    jumbled_word=jumble_word(word)
    print("the jumbled sentence is "+jumbled_word)
    guess=input("guess the word:")
    if guess == word:
        print("its correct u won !!!")

    else:
        print("oops! the word is "+word) 

play_game()
