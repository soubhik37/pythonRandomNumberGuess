import random

winNo = random.randint(0,100)
gameOver = False
guessTime = 1
guessNo = int(input(f"Please Enter a gussing number : "))
while not gameOver:
    if winNo == guessNo:
        print(f"Congress {winNo} is winning Number : You tried {guessTime}")
        gameOver = True
    else :
        if guessNo>winNo:
            print(f"Your guessing number is too high : You tried {guessTime}")
            guessTime+=1
            guessNo = int(input(f"Please guess again : "))
        elif guessNo<winNo:
            print(f"Your guessing number is too low : You tried {guessTime}")
            guessTime+=1
            guessNo = int(input(f"Please guess again : "))
        else:
            print(f"Something wrong")
            guessTime+=1
            guessNo = int(input(f"Please guess again : "))