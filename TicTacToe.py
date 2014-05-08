import struct, string

class TicTacToeBoard:

    def __init__(self):
        self.board = (['N']*3,['N']*3,['N']*3)

    def PrintBoard(self):
        print(self.board[0][0] + "|" + self.board[1][0] + "|" + self.board[2][0])
        
        print(self.board[0][1] + "|" + self.board[1][1] + "|" + self.board[2][1])
        
        print(self.board[0][2] + "|" + self.board[1][2] + "|" + self.board[2][2])

    def get_empty_squares(self):
        emptySquares = []
        for i in range(3):
            for j in range(3):
                if(self.board[i][j]=='N'):
                    emptySquares.append((i,j))
        return emptySquares

    def play_square(self, col, row, val):
        self.board[col][row] = val

    def get_square(self, col, row):
        return self.board[col][row]

    def full_board(self):
        for i in range(3):
            for j in range(3):
                if(self.board[i][j]=='N'):
                    return False
        return True

    #if there is a winner this will return their symbol (either 'X' or 'O'),
    #otherwise it will return 'N'
    def winner(self):
        #check the cols
        for col in range(3):
            if(self.board[col][0]!='N' and self.board[col][0] == self.board[col][1] and self.board[col][0]==self.board[col][2] ):
                return self.board[col][0]
        #check the rows
        for row in range(3):
            if(self.board[0][row]!='N' and self.board[0][row] == self.board[1][row] and self.board[0][row]==self.board[2][row] ):
                return self.board[0][row]
        #check diagonals
        if(self.board[0][0]!='N' and self.board[0][0] == self.board[1][1] and self.board[0][0]==self.board[2][2] ):
            return self.board[0][0]
        if(self.board[2][0]!='N' and self.board[2][0] == self.board[1][1] and self.board[2][0]==self.board[0][2]):
            return self.board[2][0]
        return 'N'

def make_simple_cpu_move(board, cpuval):
    for i in range(3):
        for j in range(3):
            if(board.get_square(i,j)=='N'):
                board.play_square(i,j,cpuval)
                return True
    return False

def play():
    Board = TicTacToeBoard()
    humanval =  'X'
    cpuval = 'O'
    Board.PrintBoard()
    
    while( Board.full_board()==False and Board.winner() == 'N'):
        print("your move, pick a row (0-2)")
        row = int(input())
        print("your move, pick a col (0-2)")
        col = int(input())

        if(Board.get_square(col,row)!='N'):
            print("square already taken!")
            continue
        else:
            Board.play_square(col,row,humanval)
            if(Board.full_board() or Board.winner()!='N'):
                break
            else:
                Board.PrintBoard()
                print("CPU Move")
                ab_decision(Board,cpuval)          ##change this
                Board.PrintBoard()

    Board.PrintBoard()
    if(Board.winner()=='N'):
        print("Cat game")
    elif(Board.winner()==humanval):
        print("You Win!")
    elif(Board.winner()==cpuval):
        print("CPU Wins!")

def playAsO():
    Board=TicTacToeBoard()
    humanval='O'
    cpuval='X'
    Board.PrintBoard()
    print("\n")

    while( Board.full_board()==False and Board.winner() == 'N'):
        minimax(Board,cpuval)              ### change this
        if(Board.full_board() or Board.winner()!='N'):
            break

        print("CPU Move")
        Board.PrintBoard()

        print("your move, pick a row (0-2)")
        row = int(input())
        print("your move, pick a col (0-2)")
        col = int(input())

        while(Board.get_square(col,row)!='N'):
            print("square already taken!")
            print("your move again, pick a row (0-2)")
            row = int(input())
            print("your move again, pick a col (0-2)")
            col = int(input())

        Board.play_square(col,row,humanval)
        if(Board.full_board() or Board.winner()!='N'):
            break
        else:
            Board.PrintBoard()
            print("\n")

    Board.PrintBoard()
    if(Board.winner()=='N'):
        print("Cat game")
    elif(Board.winner()==humanval):
        print("You Win!")
    elif(Board.winner()==cpuval):
        print("CPU Wins!")

def minimax(board,cpVal):
    if cpVal == "X":
        move,score = maxMove(board)
    else:
        move,score = minMove(board)
    board.play_square(move[0],move[1],cpVal)

def maxMove(board):
    bestScore =None
    bestMove= None
    freeSquares = board.get_empty_squares()
    for square in freeSquares:
        board.play_square(square[0],square[1],"X")
        if board.full_board() and board.winner()=='N':
            score= 0
        elif board.winner()=="X":
            score= 1
        elif board.winner()=="O":
            score= -1
        else:
            move_pos,score = minMove(board)
        
        board.play_square(square[0],square[1],"N")

        if bestScore == None or score >bestScore:
            bestScore=score
            bestMove = square
    return bestMove,bestScore

def minMove(board):
    bestScore =None
    bestMove= None
    freeSquares = board.get_empty_squares()
    for square in freeSquares:
        board.play_square(square[0],square[1],"O")
        if board.full_board() and board.winner()=='N':
            score= 0
        elif board.winner()=="X":
            score= 1
        elif board.winner()=="O":
            score= -1
        else:
            move_pos,score = maxMove(board)
        
        board.play_square(square[0],square[1],"N")

        if bestScore == None or score <bestScore:
            bestScore=score
            bestMove = square
    return bestMove,bestScore

def ab_decision(board, cpVal):
    if cpVal == "X":
        move,score = ab_max(board, float("-inf"), float("inf"))
    else:
        move,score = ab_min(board, float("-inf"), float("inf"))
    board.play_square(move[0],move[1],cpVal)

def ab_max(board, a, b):
    bestScore =None
    bestMove= None
    freeSquares = board.get_empty_squares()
    for square in freeSquares:
        board.play_square(square[0],square[1],"X")
        if board.full_board() and board.winner()=='N':
            score= 0
        elif board.winner()=="X":
            score= 1
        elif board.winner()=="O":
            score= -1
        else:
            move_pos,score = ab_min(board, a, b)
        
        board.play_square(square[0],square[1],"N")

        if bestScore == None or score > bestScore:
            bestScore = score
            bestMove = square

        if bestScore >= b:
                return bestMove,bestScore
        a = max(a, bestScore)

    return bestMove,bestScore

def ab_min(board, a, b):
    bestScore =None
    bestMove= None
    freeSquares = board.get_empty_squares()
    for square in freeSquares:
        board.play_square(square[0],square[1],"X")
        if board.full_board() and board.winner()=='N':
            score= 0
        elif board.winner()=="X":
            score= 1
        elif board.winner()=="O":
            score= -1
        else:
            move_pos,score = ab_max(board, a, b)
        
        board.play_square(square[0],square[1],"N")

        if bestScore == None or score < bestScore:
            bestScore = score
            bestMove = square

        if bestScore <= a:
                return bestMove,bestScore
        b = min(b, bestScore)

    return bestMove,bestScore

def main():
    play()

main()