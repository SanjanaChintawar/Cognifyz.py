from random import randint

def game():
    # welcome
    print("\t🎲_🎲_🎲_🎲_🎲_Welcome to The Number Guessing Game_🎲_🎲_🎲_🎲_🎲\n")
    print(
        "\tI'm Thinking of a Number Between 1 and 100 🤔 \n\t\tCan You guess It ?🧐")

    # random number
    answer = randint(1, 100)
    print(f"({answer})")
    guess = 0
    while guess != answer:
        guess = int(input("\n\tGuess the Number 👉 "))

        if guess == answer:
            print(f"\n\n\tYeah You are right 👑...It's {answer}")
        elif guess > answer:
            print("\tToo High")
        elif guess < answer:
            print("\tToo Low")


game()
