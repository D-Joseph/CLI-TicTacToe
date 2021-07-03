turn = 0 #Turn counter
#Initialize an empty game board
board = [
    ['-', '-', '-',],
    ['-', '-', '-',],
    ['-', '-', '-']]
win = False #Initialize a win boolean to false, it will be the condition for the while statement
choices = [] #Store each selected choice
while win == False: 
    row, col = input("Where do you want to move? (row column): ").split()
    while row + col in choices: #Check to see if the option was alraedy played
            row, col = input("That has already been played, choose another? (row column): ").split()
    choices.append(row + col) #If it was not already played add it to the list
    
    #Depending on whose turn it is, mark it with the corect symbol
    if turn % 2 == 1:
        board[int(row) - 1][int(col) - 1] = 'O'
    else:
        board[int(row) -1][int(col) - 1] = 'X'
    
    #Print the board
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = " ")
        print("\n")
    #Check if a horizontal or vertical line has been made, ignore a win for underscores
    for i in range(3):
         if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != '-'  or board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != '-':
            if turn % 2 == 1: #Display the winner based off the turn #
                print("O wins")
            else:
                print("X wins")
            win = True #Change the win condition to exit loop
    #Check if a diagnonal line has been made, ignore underscores 
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != '-' or board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != '-':
        if turn % 2 == 1: #Display the winner based off the turn #
                print("O wins")
        else:
            print("X wins")
        win = True #Change the win condition to exit the loop
    turn += 1 #Increase turn counter by 1


