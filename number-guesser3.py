import random

user_input = input('Guess a number between 0 and 100: ')
computer_guess = random.randint(0, 100)

def try_function(u_input):
    try:
        int(u_input)
        return True
    except:
        return False
    
while try_function(user_input) == False:
    user_input = input('Enter an integer between 0 and 100: ')

user_input = int(user_input)

while user_input != computer_guess:
    if user_input > computer_guess:
        print('Lower')
        user_input = input('New guess: ')
        while try_function(user_input) == False:
            user_input = input('Enter an integer between 0 and 100: ')
        user_input = int(user_input)
    else:
        print('Higher')
        user_input = input('New guess: ')
        while try_function(user_input) == False:
            user_input = input('Enter an integer between 0 and 100: ')
        user_input = int(user_input)

print('Youhou')
        


    


# if it's the right type, play the game