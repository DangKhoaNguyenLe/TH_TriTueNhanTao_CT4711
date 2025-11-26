from ast import Pow
import os, math
import sys

def checWinkCols(board, n):
    for i in range(n):
        c = board[i]  
        check = 0
        for j in range(i, n*n, n):  
            if board[j] == c: 
                check += 1
        if check == n:  
            return c
    return None

def checkWinRows(board, n):
    for i in range(0, n*n, n):  
        c = board[i]  
        check = 0
        for j in range(i, i + n):  
            if board[j] == c: 
                check += 1
        if check == n:  
            return c
    return None

def checkWinCheoChinh(board, n):
    c = board[0]
    check = 0
    for i in range(0, n*n, n + 1):  
        if board[i] == c:
            check += 1
    if check == n:  
        return c
    return None

def checkWinCheoPhu(board, n):
    c = board[n-1]
    check = 0
    for i in range(n-1, (n*n)-(n-1), n-1):  
        if board[i] == c:
            check += 1
    if check == n:  
        return c
    return None

def GetWinner(board, n):
    if checWinkCols(board, n) is not None:
        return checWinkCols(board, n)
    if checkWinRows(board, n) is not None:
        return checkWinRows(board, n)
    if checkWinCheoChinh(board, n) is not None:
        return checkWinCheoChinh(board, n)
    if checkWinCheoPhu(board, n) is not None:
        return checkWinCheoPhu(board, n)
    return None


def PrintBoard(board, n):
    os.system('cls' if os.name=='nt' else 'clear')
    size = (n*n)
    for i in range(0,size):  
        print(f"{board[i]}\t", end="|")
        
        if (i + 1) % n == 0:
            print()
        
    
def GetAvailableCells(board):
    available = list()
    for cell in board:
        if cell != "X" and cell != "O":
                available.append(cell)
    return available

def minimax(position, depth, alpha, beta, isMaximizing, n):
    if depth > n: 
      return 0
    winner = GetWinner(position, n)
    if winner != None:
        return n*n - depth if winner == "X" else -(n*n) + depth
    if len(GetAvailableCells(position)) == 0:
        return 0
    if isMaximizing:
        maxEval = -math.inf
        for cell in GetAvailableCells(position):
            position[cell - 1] = "X"
            Eval = minimax(position, depth + 1, alpha, beta, False, n)
            maxEval = max(maxEval, Eval)
            alpha = max(alpha, Eval)
            position[cell - 1] = cell
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = +math.inf
        for cell in GetAvailableCells(position):
            position[cell - 1] = "O"
            Eval = minimax(position, depth + 1, alpha, beta, True, n)
            minEval = min(minEval, Eval)
            beta = min(beta, Eval)
            position[cell - 1] = cell
            if beta <= alpha:
                break # prune
    return minEval

def FindBestMove(currentPosition, AI, n):
    bestVal = -math.inf if AI == "X" else +math.inf
    bestMove = -1
    for cell in GetAvailableCells(currentPosition):
        currentPosition[cell - 1] = AI
        moveVal = minimax(currentPosition, 0, -math.inf, +math.inf, False if AI == "X" else True, n)
        currentPosition[cell - 1] = cell
        if (AI == "X" and moveVal > bestVal):
            bestMove = cell
            bestVal = moveVal
        elif (AI == "O" and moveVal < bestVal):
            bestMove = cell
            bestVal = moveVal
    return bestMove

def main():
    player = input("Play as X or O? ").strip().upper()
    AI = "O" if player == "X" else "X"
    n = int(input("Ma trận NxN: "))
    currentGame = [*range(1, (n*n)+1)]
    currentTurn = "X"
    counter = 0
    while True:
        if currentTurn == AI:
            cell = FindBestMove(currentGame, AI, n)
            currentGame[cell - 1] = AI
            currentTurn = player
        elif currentTurn == player:
            while True:
                PrintBoard(currentGame,n)
                input_user = input("Enter Number: ").strip()
                humanInput = int(input_user)
                if humanInput in currentGame:
                    currentGame[humanInput - 1] = player
                    currentTurn = AI
                    break
                else:
                    PrintBoard(currentGame, n)
                    print("ô dả được đánh")
        if GetWinner(currentGame, n) != None:
            PrintBoard(currentGame, n)
            print(f"{GetWinner(currentGame, n)} Win")
            break
        counter += 1
        if GetWinner(currentGame, n) == None and counter == (n*n)-1:
            PrintBoard(currentGame,n)
            print("Hòa")
            break
        
if __name__ == "__main__":
    main()