import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f""" Welcome to the Bagle game.

    I have three digit number on my mind, where no of the digits are the same. Try to guess it!

    Hints:
    "pico" means one digit is correct but it's placed wrong
    "fermi" means one digit is correct and it's in the right place
    "bagel" means none of the digits are correct 

    You have {MAX_GUESSES} tries.
    Good luck!
    """)

    while True:
        secretNum = getSecretNum()
        print(f"Try to guess a number. You have {MAX_GUESSES} tries")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Try number #{}".format(numGuesses))
                guess = input("> ")
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You used all of your tries")
                print("Correct answer is {}".format(secretNum))
    
        print("Do you want to play again ?")
        if not input("> ").lower().startswith("t"):
            break
    
    print("Thanks for playing!")

def getSecretNum():
    """Returns random number for player to guess"""
    numbers = list("0123456789")
    random.shuffle(numbers)

    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num

def getClues(guess, secretNum):
    """Returns hint basen on guess"""
    if guess == secretNum:
        return "Succes!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagle"
    else:
        clues.sort()
        return "".join(clues)
    
if __name__ == "__main__":
    main()