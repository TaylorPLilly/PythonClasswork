import random
print('Welcome to the higher/lower game, Bella!')
lower = int(input('Enter the lower bound: '))
higher = int(input('Enter the upper bound: '))
random_number = random.randint(lower, higher)
print('Great, now guess a number between {0} and {1}: '.format(lower, higher))
guess = int(input())
while guess != random_number:
	if guess < random_number:
		print(guess)
		print ('Nope, too low.')
		print()
		guess = int(input('Guess another number: '))
	if guess > random_number:
		print(guess)
		print('Nope, too high.')
		print()
		guess = int(input('Guess another number: '))
	if guess == random_number:
		print('You got it!')
		break
