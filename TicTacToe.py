"""
Author: abraham-milgram
Description: Runs a random tic-tac-toe game a given amount of times.
"""
import random
# Generates a random game of tic-tac-toe
def boardGen():
    moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    player = 'x'

    for i in range(9):
        while True:
            moveRow = random.randint(0, 2)
            moveColumn = random.randint(0, 2)
            mNumber = moveRow * 3 + moveColumn
            if mNumber in moves:
                moves.remove(mNumber)
                break
        
        board[moveRow][moveColumn] = player
        
        if player == 'x':
            player = 'o'
        else:
            player = 'x'

    return board

# Win detection
def win(board):
    # Checking rows for wins
    for r in board:
        if len(set(r)) == 1:
            return r[0]

    # Checking columns for wins
    for c in range(3):
        column = []
        for r in range(3):
            column.append(board[r][c])
        if len(set(column)) == 1:
            return column[0]
    # Checking diagonal from top left to bottom right for wins
    diagonal = []
    for c in range(3):
        column.append(board[c][c])
    if len(set(diagonal)) == 1:
        return diagonal[0]
    # Checking diagonal from top right to bottom left for wins
    diagonal = []
    for c in range(3):
        column.append(board[2 - c][2 - c])
    if len(set(diagonal)) == 1:
        return diagonal[0]
# Main: prompts user for how many times to run the simulation and runs the board gen the amount of times the user specifies
# Finally, it presents the results and overall winner of the simulation
def main():
    while True:
        try:
            r = int(input("How many times do you want to run simulation? "))
            break
        except:
            pass

    x = 0
    o = 0
    for i in range(r):
        winner = win(boardGen())
        if winner == 'x':
            x += 1
        else:
            o += 1
    w = 'x'
    if x > o:
        pass
    elif o > x:
        w = 'o'
    else:
        w = 'tie'

    print(f"""
    Simulation ran {r} times.
    x won {x} times.
    o won {o} times.
    Winner: {w}
    """)

if __name__ == "__main__":
    main()