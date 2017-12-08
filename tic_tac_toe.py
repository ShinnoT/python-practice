#create empty board (list) with 9 spaces
board = [" " for i in range(9)]
  #this is equivalent to
  #board = []
  #for i in range(9)
    #board.append(" ")

def print_board():
  row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
  row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
  row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

  print()
  print(row1)
  print(row2)
  print(row3)
  print()

def player1(choice):
  if board[choice - 1] != " ":
    print("that space is already taken")
    choice = int(input("enter your move player1: 1-9 --> ").strip())
    board[choice - 1] = "X"
  else:
    board[choice - 1] = "X"

def player2(choice2):
  if board[choice2 - 1] != " ":
    print("that space is already taken")
    choice2 = int(input("enter your move player2: 1-9 --> ").strip())
    board[choice2 - 1] = "O"
  else:
    board[choice2 - 1] = "O"

while True:
  print_board()
  choice = int(input("enter your move player1: 1-9 --> ").strip())
  player1(choice)
  print_board()
  choice2 = int(input("enter your move player2: 1-9 --> ").strip())
  player2(choice2)
