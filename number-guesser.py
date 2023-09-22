import random

print("Welcome to the number guesser game. Please write a range to guess from in this format: 'X-X'")

user_input = input(">>>")
range_numbers = user_input.split("-")
range_numbers[0] = int(range_numbers[0])
range_numbers[1] = int(range_numbers[1])
guesses = 0

computer_choice = random.randint(range_numbers[0], range_numbers[1])

print("The computer has now chosen a number within your range. Guess a number, and it'll tell you if the actual number is lower or high")
user_input = int(input(">>>"))

while user_input != computer_choice:
	if user_input > computer_choice:
		print("Lower")
		guesses += 1
		user_input = int(input(">>>"))
	elif user_input < computer_choice:
		print("Higher")
		guesses += 1
		user_input = int(input(">>>"))

if user_input == computer_choice:
	print("You won in " + str(guesses) + " guesses!")