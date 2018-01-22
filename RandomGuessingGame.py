import random

ivHighest = 10
ivAnswer = random.randint(1,ivHighest)
ivGuess = 0
print("Please guess a number between 1 and {}: ".format(ivHighest))
while ivGuess != ivAnswer:
    ivGuess = int(input())
    if ivGuess == 0:
        print("Give up eh?")
        break
    elif ivGuess > ivAnswer:
        print("Guess lower")
    elif ivGuess < ivAnswer:
        print("Guess higher")
    else:
        print("YOU GUESSED IT!")




