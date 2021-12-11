import random


name = input("Hi! What's your name?")
computer_number = random.randint(-100, 100)
count = 0
while True:
    guess = int(input(f"Ok. Print your guess from -100 to 100, {name}"))
    if guess > computer_number:
        print('Its smaller')
        count += 1
    elif guess < computer_number:
        print('Its bigger ')
        count += 1
    elif guess == computer_number:
        print(f'You win, attempts: {count}')
        print('Thanks for the game')
        break





# if guess != computer_number:
#     print('I win')
# else:
#     print('You win')



 






