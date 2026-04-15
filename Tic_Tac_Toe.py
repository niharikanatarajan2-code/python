board=['']*9
def printBoard():
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[0]}|{board[1]}|{board[2]}")
def checkWin():
    wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
     if board[a]==board[b]==board[c] and board[a]!='':
        return True
    return False
def game():
    turn='X'
    for i in range (9):
        printBoard()
        move=int(input(f"Turn {turn}, choose(1-9):"))-1
        if board[move] != '':
           print("Aldraedy filled, Try again")
           continue  
        board[move]=turn
        if i >= 4 and checkWin():
         printBoard()
         print(f"{turn} wins!")
         return
        turn='O' if turn=='X' else 'X'
    printBoard()
    print("It's a tie")
game()