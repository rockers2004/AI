def is_safe(board, row, col):
    #Bounding : Checking if the column is already occupied
    for i in range(col):
        if board[row][i] == 'Q':
            return False
        
    for j, k in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[j][k] == 'Q':
            return False
    for j, k in zip(range(row, len(board)), range(col, -1, -1)):
        if board[j][k] == 'Q':
            return False
        
    return True

def printBoard(board):
    for row in board:
        print(" ".join(row))
    print("\n" + "`" * (2*len(board)-1) + "\n")

def solve(board, row, solutions):
    if row == len(board): #Base Case : All Queens placed
        solutions.append(row[:] for row in board)
        printBoard(board)
        return
    
    for col in range(len(board)): #Branching: Trying all columns
        if is_safe(board, row, col): #Pruning: Only proceed if safe
            board[row][col] = 'Q'
            solve(board, row+1, solutions) #Recursive call for next row
            board[row][col] = '_' #Backtracking: Undoing move for searching next possibility



if __name__=="__main__":
    n = int(input("Enter N : "))
    board = [['_']*n for _ in range(n)]
    solutions = []
    solve(board, 0, solutions)
    print(f'Total Solutions : {len(solutions)}')