from random import randint

import sys


while True:
    try:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level <=0:
            continue

        else:
            gen = randint(1, level)
           
            try:
                guess= int(input("Guess: "))
                if guess==gen:
                    print("Just right!")
                    sys.exit()
                elif guess< gen:
                    print("Too small!")
                else:
                    print("Too large!")
            except ValueError:
                continue

    except EOFError:
        break
    else:
        continue



