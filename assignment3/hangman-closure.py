# Task 4
def make_hangman(secret_word: str):
    guesses = []
    
    def hangman_closure(letter: str):
        if len(letter) < 0 or len(letter) > 1:
            print("Guess must be one letter")
            return False
        
        guesses.append(letter)
        progress = "".join([char if char in guesses else "_" for char in secret_word])
        print(progress)
        return "_" not in progress
    
    return hangman_closure


hangman_one = make_hangman("alphabet")

while True:
    if hangman_one(input("Guess a letter: ")):
        break