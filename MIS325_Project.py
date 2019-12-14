import random

#TODO
def pos_to_idx(pos):
  pos = int(pos)
  if pos < 0 or pos > 8:
    return (-1, -1)
  # first find row num
  row = -1
  col = -1
  if pos >= 6:
    row = 2
  elif pos >= 3:
    row = 1
  elif pos >= 0:
    row = 0
  
  # next find col num
  col = pos % 3
  return (row, col)

def check_valid(pos, board):
  if pos == '' or not pos.isnumeric():
    return False
  pos = int(pos)
  row, col = pos_to_idx(pos)
  return pos >= 0 and pos <= 8 and (board[row][col] == 0)

def comp_move(board):
  # get all available positions
  avail = list()
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        avail.append((i, j))
  return avail[random.randrange(len(avail))]

#return player num on winner, 0 on draw, >1 on no winner
def check_winner(board):
  # check rows
  for i in range(len(board)):
    if board[i][0] == 1 and board[i][1] == 1 and board[i][2] == 1:
      return 1
    if board[i][0] == -1 and board[i][1] == -1 and board[i][2] == -1:
      return -1
  # check columns
  for j in range(len(board)):
    if board[0][j] == 1 and board[1][j] == 1 and board[2][j] == 1:
      return 1
    if board[0][j] == -1 and board[1][j] == -1 and board[2][j] == -1:
      return -1
  # check diagonals
  if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
    return 1
  if board[0][0] == -1 and board[1][1] == -1 and board[2][2] == -1:
    return -1
  
  if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
    return 1
  if board[0][2] == -1 and board[1][1] == -1 and board[2][0] == -1:
    return -1
  
  # check for draw
  no_spot = True
  for row in board:
    if 0 in row:
      no_spot = False
  if no_spot:
    return 0
  return 2

def is_no_winner(board):
  return check_winner(board) > 1

def is_winner(board):
  return check_winner(board) <= 1

def invalid_move(move, board):
  return not check_valid(move, board)

def print_board(board):
  board_pos = 0
  print('Board')
  print('-------------')
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        print(str(board_pos), end=' ')
      elif board[i][j] == 1:
        print('X', end=' ')
      elif board[i][j] == -1:
        print('O', end=' ')
      board_pos += 1
    print()

#TODO
board = list()
player_token = 1
comp_token = -1
# Initialize the game
# The player holds the spot if there is a 1 on the board
# The computer holds the spot if there is a -1 on the board
# First, set board to be a list of 3 lists, each list has 0 zeroes
board = [[0,0,0],[0,0,0],[0,0,0]]
# Then, print the board to console
print_board(board)
# ===Create the game loop===
# While there is no winner on the board
while is_no_winner(board):
  # Ask the user for a move (maybe put a prompt saying "Choose a position>> ")
  m = input('Enter move>> ')
  # While the user has input an invalid move
  while invalid_move(m, board):
    m = input('Enter new move>> ')
  # Ask again for another move (maybe put a prompty saying "Choose another position>> ")
  
  # Convert the move into board indexes
  #   Note: if a function returns a tuple like
  #   def foo(): 
  #     return (1, 2)
  #   You can get 1 and 2 separately by doing:
  #   x, y = foo() so x will be 1 and y will be 2
  r, c = pos_to_idx(m)

  # Set the board's value at that position to the player token
  print('Player Move', end=' | ')
  board[r][c] = 1
  # Print the board again to show the new move
  print_board(board)

  # If there is a winner after that move was made, exit the loop
  if is_winner(board):
    break  
  print('Computer Move', end=' | ')
  # Get the computer's next move
  r, c = comp_move(board)

  # Set the board at the computer's chosen position to the computer token
  board[r][c] = -1
  # Print the board again to show the computer's move
  print_board(board)

# The code below checks for a winner
code = check_winner(board)
if code == 1:
  print('Player wins!')
elif code == -1:
  print('Computer wins!')
elif code == 0:
  print('Draw!')



