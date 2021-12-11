import random

name = input("Hi! What's your name?")
computer_number = random.randint(-100,100)
while True:
    guess = int(input(f"Ok. Print your guess from -100 to 100, {name}"))
    if guess > computer_number:
        print('Its smaller')
    elif guess < computer_number:
        print('Its bigger ')
else:
    print('You win')



# if guess != computer_number:
#     print('I win')
# else:
#     print('You win')



 






