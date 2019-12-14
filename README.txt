Gracie Eiseman
B00646568

# first find row num
# next find col num
# get all available positions
#return player num on winner, 0 on draw, >1 on no winner
# check rows
# check columns
# check diagonals
# check for draw

# Initialize the game
# The player holds the spot if there is a 1 on the board
# The computer holds the spot if there is a -1 on the board
# First, set board to be a list of 3 lists, each list has 0 zeroes
# Then, print the board to console
# ===Create the game loop===
# While there is no winner on the board
# Ask the user for a move (maybe put a prompt saying "Choose a position>> ")
# While the user has input an invalid move
# Ask again for another move (maybe put a prompty saying "Choose another position>> ")
  
# Convert the move into board indexes
#   Note: if a function returns a tuple like
#   def foo(): 
#     return (1, 2)
#   You can get 1 and 2 separately by doing:
#   x, y = foo() so x will be 1 and y will be 2
# Set the board's value at that position to the player token
# Print the board again to show the new move
# If there is a winner after that move was made, exit the loop
# Get the computer's next move
# Set the board at the computer's chosen position to the computer token
# Print the board again to show the computer's move
# Then code checks for a winner