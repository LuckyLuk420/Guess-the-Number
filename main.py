from random import randint

num = randint(1, 100)
tries = []


while True:
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            tries.append(guess)
            break
        except:
            print("\n!!!\nPlease only enter an integer between 1 and 100\n!!!\n")
            continue
    if guess == num:
        print("CONGRATULATIONS!!! It took you just {} tries, fool!".format(len(tries)))
        break
    elif guess < num:
        print("Too small")
        print("You already guessed:\n{}\n".format(tries))
        continue
    elif guess > num:
        print("Too big")
        print("You already guessed:\n{}\n".format(tries))
        continue
