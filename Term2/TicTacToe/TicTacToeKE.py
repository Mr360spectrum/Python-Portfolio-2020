# Karter Ence
# Tic Tac Toe
# 11/7/2019
import random

X = "X"
O = "O"
NUM_SQUARES = 9
TIE = "TIE"
EMPTY = " "

def instructions():
    """Display game instructions."""
    print(
    """
    Welcome to the greatest intellectual challenge of all time.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move by entering a number, 1 - 9. The number
    will correspond to the board position as positioned:

                    1 | 2 | 3 
                    ---------
                    4 | 5 | 6
                    ---------
                    7 | 8 | 9

    Prepare yourself, human. The ultimate battle is about to begin. \n
    """)

def ask_YN(question):
    """Ask a yes or no question and give a one letter response."""
    response = None
    while response not in ("y", "n", "yes", "no"):
        response = input(question).lower()
    x = response[0]
    return x

def new_board():
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print(str.format("""
     {0} | {1} | {2} 
     ---------
     {3} | {4} | {5}
     ---------
     {6} | {7} | {8}
    """, board[0], board[1], 
        board[2], board[3], 
        board[4], board[5], 
        board[6], board[7], 
        board[8]))

def pieces():
    go_first = ask_YN("Would you like to go first?")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        comp = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        comp = X
        human = O
    return comp, human

def ask_number(question, low, high):
    response = None
    while response not in range(low, high + 1):
        try:
            response = int(input(question))
        except:
            print("That is not a number.")
    return response

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (1 - 9): ", 0,  NUM_SQUARES) - 1
        if move not in legal:
            print("You fool. You absolute moron. Can you not tell what's going on? Get your eyes and brain checked and try again, you know, sometime today.")
    print("Fine...")
    return move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def winner(board):
    """Determine the game winner"""
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        # Make sure all squares in a combination are filled with the same character
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            # Winner equals whichever piece is at row[0]
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def congrat_winner(board):
    win = winner(board)
    if win == TIE:
        print("Oh, dear. It seems that we have tied. That's only because I messed up two turns ago.")
    if win == X:
        print("Congratulations! You win! Although, that's only because you cheated.")
    elif win == O:
        print("Just as I have foreseen. You lost. git gud lol")

def comp_move(board, human, comp):
    # Make a copy of the board
    board_copy = board[:]
    # Best positions, in order to give the computer different difficulties
    MOVES1 = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    MOVES2 = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    MOVES3 = (0, 2, 6, 8, 4, 1, 3, 5, 7)
    allMoves = [MOVES1, MOVES2, MOVES3]
    randMoves = random.choice(allMoves)
    print("I shall take square number", end=" ")
    # If computer can win, take that move
    for move in legal_moves(board):
        board_copy[move] = comp
        if winner(board_copy) == comp:
            print(move + 1)
            return move
        board_copy[move] = EMPTY
    # If human can move, stop them
    for move in legal_moves(board):
        board_copy[move] = human
        if winner(board_copy) == human:
            print(move + 1)
            return move
        board_copy[move] = EMPTY
    for move in randMoves:
        if move in legal_moves(board):
            print(move + 1)
            return move

def game():
    instructions()
    comp, human = pieces()
    board = new_board()
    if human == X:
        turn = human
    else:
        turn = comp
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, turn)
            board[move] = human
            display_board(board)
            turn = next_turn(turn)
        else:
            move = comp_move(board, human, comp)
            board[move] = comp
            display_board(board)
            turn = next_turn(turn)
    winner(board)
    congrat_winner(board)
game()
