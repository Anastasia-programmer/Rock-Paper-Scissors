import random
emojis={
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌"
}

numberOfTrials=roundNumber=1
numberOfWins=numberOfLosses=numberOfDraws=0
numberofplayers=1
options=["rock", "paper","scissors"]
print(" Welcome to the Rock, Paper, Scissors game! ")

while True:
 numberofplayers=input("choose 1 for one player mode and 2 for two players mode:")
 def show_leaderboard():
    print("\nLeaderboard:")
    try:
        with open("game_results.txt", "r") as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("file not found!")
 if numberofplayers=="1" :
  print("Please enter your name:")
  userName = input().strip()
  print(" You will play against the computer.")
  while True :
    print("Round ", roundNumber," :");
    computerGuess=random.choice(options)
    userGuess=input("Please enter your guess : Paper , Rock , or Scissors :")
    userGuess=userGuess.lower().strip()
    if userGuess not in options :
        print("Invalid input , please try again.")
        continue
    if computerGuess == "rock" and userGuess == "scissors" or computerGuess== "scissors" and userGuess == "paper" or computerGuess == "paper" and userGuess == "rock":
        print("Oh no Computer Wins!" ,computerGuess ,emojis[computerGuess] ,"beats " , userGuess ,emojis[userGuess],"hhhh")
        
        numberOfLosses += 1
    elif computerGuess == userGuess:
        print("ّIt is a draw , you both chose : ", userGuess ,emojis[userGuess])
        
        numberOfDraws += 1
    else:
        print("Yeeeey Congratulations! You win! ", userGuess ,emojis[userGuess], "beats", computerGuess ,emojis[computerGuess])
        numberOfWins += 1
    playAgain=input("Do you wanna play again Y/N ? ").upper()
    while True:
            if playAgain == "Y":
                roundNumber += 1
                numberOfTrials += 1
                break
            elif playAgain == "N":
                print("Thanks for playing! You played ",roundNumber,"Rounds with", numberOfTrials, "trials  and your score is:")
                print("Wins:", numberOfWins, "\nLosses:", numberOfLosses, "\nDraws:", numberOfDraws)
                with open("game_results.txt", "a") as file:
                    file.write(f"{userName} played {roundNumber} rounds with {numberOfTrials} trials. Wins: {numberOfWins}, Losses: {numberOfLosses}, Draws: {numberOfDraws}\n")
                print("Your results have been saved to game_results.txt")
                show_leaderboard()
                exit()
            else:
              playAgain=input("Invalid input, please enter Y or N.").upper()
  
 elif numberofplayers=="2":
    playerOneWins=playerTwoWins=playerOneLosses=playerTwoLosses=Draws=0
    roundNumber=1
    print(" You will play against anothe player:")
    print("Player-One, please enter your name:")
    playerOneName = input().strip()
    print("Player-Two, please enter your name:")
    playerTwoName = input().strip()
    while True: 
     print("Round ", roundNumber," :");
     playerOneGuess=input("Player-One Please enter your guess : Paper , Rock , or Scissors :")
     playerOneGuess=playerOneGuess.lower().strip()
     if playerOneGuess not in options :
        print("Invalid input , please try again.")
        continue
     else : 
        print("\n" * 50)
        while True:
         playerTwoGuess=input("player-Two Please enter your guess : Paper , Rock , or Scissors :")
         if playerTwoGuess not in options :
          print("Invalid input , please try again.")
          continue
         else:
          playerTwoGuess=playerTwoGuess.lower().strip()
          break
        if playerOneGuess == "rock" and playerTwoGuess == "scissors" or playerOneGuess== "scissors" and playerTwoGuess == "paper" or playerOneGuess == "paper" and playerTwoGuess == "rock":
            print("Player-One Wins!" ,playerOneGuess ,emojis[playerOneGuess] ,"beats " , playerTwoGuess ,emojis[playerTwoGuess],"hhhh")
            
            playerOneWins+=1
            playerTwoLosses+=1
        elif playerOneGuess == playerTwoGuess:
            print("ّIt is a draw , you both chose : ", playerOneGuess ,emojis[playerOneGuess])
            
            Draws+=1
        else:
            print("Player-Two Wins! ", playerTwoGuess ,emojis[playerTwoGuess], "beats", playerOneGuess ,emojis[playerOneGuess])
            playerTwoWins+=1
            playerOneLosses+=1
        playAgain=input("Do you wanna play again Y/N ? ").upper()
        while True:
            if playAgain == "Y":
                roundNumber += 1
                numberOfTrials += 1
                break
            elif playAgain == "N":
                print("Thanks for playing! You played ",roundNumber,"Rounds and your score is:")
                print("Player-One Wins:", playerOneWins, "\nPlayer-Two Wins:", playerTwoWins, "\nDraws:", Draws)
                print("Player-One Losses:", playerOneLosses, "\nPlayer-Two Losses:", playerTwoLosses)
                with open("game_results.txt","a") as file:
                    file.write(f"{playerOneName} played {roundNumber} rounds  won: {playerOneWins}, lost: {playerOneLosses} with {playerTwoName} who won: {playerTwoWins}, lost: {playerTwoLosses}, and for draws: {Draws}\n ")
                print("Your results have been saved to game_results.txt")
                show_leaderboard()
               
                exit()
            else:
              playAgain=input("Invalid input, please enter Y or N.").upper()

 else:
    print("Invalid input, please choose 1 or 2 for number of players.")
    
  



         

    
    


