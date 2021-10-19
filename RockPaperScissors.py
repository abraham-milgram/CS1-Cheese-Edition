import random

def main():

    # User input loop preventing invalid values
    while True:
        user = input("Rock, Paper, or Scissors (\"rock\", \"paper\", or \"scissors\"): ")

        if user not in ('rock', 'paper', 'scissors'):
            print("Input Invalid: please us a value of \"rock\", \"paper\", or \"scissors\"")
        else:
            break
    
    # Randomly generates bot's move and prints it
    moves = ['rock', 'paper', 'scissors']
    random.shuffle(moves)
    bot = moves[0]
    print(f"Bot chose: {bot}")

    # Conditions in which the bot wins
    botConditions = (('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock'))

    # Loops if bot == user 
    if bot == user:
        print("You chose the same thing!")
        main()
    # If the scenerio is in botConditions than the bot wins if not the player wins
    elif (bot, user) in botConditions:
        print("Bot wins!")
    else:
        print("Player wins!")

if __name__ == '__main__':
    main()