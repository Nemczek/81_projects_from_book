import random

NUM_OF_DIGITS = 3
GUESSES = 10

def main():
    print(f"""Welcome to Bagle game!
    I have a three digit number in my mind, try to guess it !
    You have {GUESSES} tries.
    Good luck!
    
    Hints:
    "pico" means one digit is correct but it's placed wrong
    "fermi" means one digit is correct and it's in the right place
    "bagel" means none of the digits are correct\n""")

    while True:
        secNum = generateNumber()
        num_of_guesses = 1

        while num_of_guesses <= GUESSES:
            print(f"Try number {num_of_guesses}")
            guess = getGuess()
            num_of_guesses += 1

            if guess != secNum:
                hints = "".join(giveHints(secNum, guess))
                print(hints)
            else:
                print("Congratulations!")
                break

            if num_of_guesses > GUESSES:
                print(f"You used all of your tries. The correct answer is {secNum}")
    
        print("Do you want to play again? (y/n)")
        if not input("> ").lower().startswith("y"):
            break

def getGuess():
    """Function to get guess from player"""
    guess = input("> ")
    
    while True:
        if len(guess) == NUM_OF_DIGITS and guess.isdecimal():
            break
        print("You typed wrong asnwer! Please remember that asnwer should be a three digit number.")
        guess = input("> ")
    
    return guess

def generateNumber():
    """Function to generate number"""
    number = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    random.shuffle(numbers)

    for i in numbers:
        if i not in number and len(number) != NUM_OF_DIGITS:
            number.append(i)
    
    return "".join(number)

def giveHints(generatedNumber, guess):
    """Function to generate hints based on given guess"""
    hints = []
    for i in range(len(guess)):
        if guess[i] == generatedNumber[i]:
            hints.append("Fermi")
        elif guess[i] in generatedNumber:
            hints.append("Pico")
        if len(guess) == 0:
            return "Bagle"
    return hints

if __name__ == "__main__":
    main()