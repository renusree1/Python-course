board= {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}
board_keys = []
for key in board:
    board_keys.append(key)  

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(board)
        print("Its your turn!" + turn + " Move to which place?")
        move = input()

        if move not in board_keys:
            print("Invalid move! Please choose a number between 1-9.")
            continue

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ' and board['7'] == turn:
                printBoard(board)
                print("Game Over.\n")
                print(" ****** " + turn + " won ******")
                break
            elif board['4'] == board['5'] == board['6'] != ' ' and board['4'] == turn:
                printBoard(board)
                print("Game Over.\n")
                print(" ****** " + turn + " won ******")
                break
            elif board['1'] == board['2'] == board['3'] != ' ' and board['1'] == turn:
                printBoard(board)
                print("Game Over.\n")
                print(" ****** " + turn + " won ******")
                break
            elif board['1'] == board['4'] == board['7'] != ' ' and board['1'] == turn:
                printBoard(board)
                print("Game Over.\n")
                print(" ****** " + turn + " won ******")
                break
            elif board['2'] == board['5'] == board['8'] != ' ' and board['2'] == turn:
                printBoard(board)
                print("Game Over.\n")
                print(" ****** " + turn + " won ******")
                break
            elif board['3'] == board['6'] == board['9'] != ' ' and board['3'] == turn:
                printBoard(board)
                print("Game Over.\n")
                print(" ****** " + turn + " won ******")
                break
            elif board['1'] == board['5'] == board['9'] != ' ' and board['1'] == turn:
                printBoard(board)
                print("Game Over.\n")
                print(" ****** " + turn + " won ******")
                break
            elif board['7'] == board['5'] == board['3'] != ' ' and board['7'] == turn:
                printBoard(board)
                print("Game Over.\n")
                print(" ****** " + turn + " won ******")
                break

        if count == 9:
            printBoard(board)
            print("\nGame over\n")
            print("It's a Tie!!")
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to play Again? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            board[key] = " "
        game()
if __name__ == "__main__":
    game()