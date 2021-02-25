from random import randint

print('Welcome to the Number Guessing Game!')
print('I\'m thinkin of a number between 1 and 100')
def mainGame():
    print('10 for easy and 5 for hard')
    inputLevel = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    guessValue = randint(0,100)
    easyValue = 10
    hardValue = 5
    if inputLevel=='easy':
        print(f'You have {easyValue} attempts remaining to guess the number.')

        # This will be execute win user choose difficulty easy
        guess = int(input('Make a guess: '))
        for v in range(easyValue,0,-1): 
            if guess==guessValue:
                # if input value are match this print You win 
                print("You win") 
                break
            else:
                if guess > guessValue:
                    # if guess value gater then orginal guess value
                    print("Too high")
                    easyValue -= 1
                else:
                    # if guess value less then orginal guess value
                    print("Too Low")
                    easyValue -= 1
                    # by defualt print this value when the input value too High or too Low
                print(f"You have {v-1} attempts remaining to guess the number")
                guess = int(input('Guess Again : '))
    elif inputLevel=='hard':
        print(f'You have {hardValue} attempts remaining to guess the number.')

        guess = int(input('Make a guess: '))
        for v in range(hardValue,0,-1):
            if guess==guessValue:
                # if input value are match this print You win 
                print("You win") 
                break
            else:
                if guess > guessValue:
                    # if guess value gater then orginal guess value
                    print("Too high")
                    easyValue -= 1
                else:
                    # if guess value less then orginal guess value
                    print("Too Low")
                    easyValue -= 1
                    # by defualt print this value when the input value too High or too Low
                print(f"You have {v-1} attempts remaining to guess the number")
                guess = int(input('Guess Again : '))

    else:
        print('you enter wrong option try again')
        mainGame()
mainGame()
