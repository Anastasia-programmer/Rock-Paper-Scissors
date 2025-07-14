import random
emojis={
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌"
}
computerGuess=userGuess="Paper"
roundNumber=1
numberOfTrials=1
playAgain="Y"
print(" Welcome to the Rock, Paper, Scissors game! ")
print("You will play against the computer.")
options=["rock ", "paper","scissors"]
while True :
    print("Round :", roundNumber);
    computerGuess=random.choice(options)
    userGuess=input("Please enter your guess : Paper , Rock , or Scissors :")
    userGuess=userGuess.lower()
    if userGuess not in options :
        print("Invalid input , please try again.")
        continue
    if computerGuess == "Rock" and userGuess == "Scissors" or computerGuess== "Scissors" and userGuess == "Paper" or computerGuess == "Paper" and userGuess == "Rock":
        print("Oh no Computer Wins!" ,computerGuess ,emojis[computerGuess] ,"beats " , userGuess ,emojis[userGuess],"hhhh")
        numberOfTrials += 1
    elif computerGuess == userGuess:
        print("ّIt is a draw , you both chose : ", userGuess ,emojis[userGuess])
        numberOfTrials += 1
    else:
        print("Yeeeey Congratulations! You win! ", userGuess ,emojis[userGuess], "beats", computerGuess ,emojis[computerGuess])
    playAgain=input("Do you wanna play again Y/N ? ").upper()
    while True:
            if playAgain == "Y":
                roundNumber += 1
                break
            elif playAgain == "N":
                print("Thanks for playing! You played ",roundNumber,"Rounds with", numberOfTrials, "trials ")
                exit()
            else:
              playAgain=input("Invalid input, please enter Y or N.").upper()
         

    
    


