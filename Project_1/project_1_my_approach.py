import random

NUM_OF_DIGITS = 3
GUESSES = 10

def main():
    print(f"""Welcome to Bagle game!
    I have a three digit number in my mind, try to guess it !
    You have {GUESSES} number of guesses.
    Good luck!
    """)
    secNum = generateNumber()

    num_of_tries = 0
    while True:
        if num_of_tries != GUESSES:
            guess = getGuess()
            num_of_tries += 1





def getGuess():
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
    for i in enumerate(guess):
        if guess[i] == generatedNumber[i]:
            hints.append("Fermi")
        elif guess[i] in generatedNumber:
            hints.append("Pico")
        else:
            return "Bagle"
    return hints





"""
Plan
1. Wytłumacz o co chodzi w grze
2. funkcja do losowania liczby (najlepiej bez powtórzeń)
3. funkcja do pobierania odpowiedzi
4. sprawdzać aby dane się zgadzały
5. funkcja do printowania podpowiedzi
6. Mainloop ze sprawdzaniem odpowiedzi
"""