# Task 6
class TictactoeException(Exception):
    def __init__(self, message: str, *args: object) -> None:
        self.message = message
        super().__init__(*args)
        
        
class Board():
    #DO NOT EDIT POSITION
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
    
    def __init__(self) -> None:
        self.board_array = [["" for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        
    def move(self, move_string: str):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column
        
        if self.board_array[row][column] != "":
            raise TictactoeException("That spot is taken.")
        
        self.board_array[row][column] = self.turn
        
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
            
    def whats_next(self):
        cat = True
        
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == "":
                    cat = False
                    break
        
        if (cat):
            return (True, "Cat's Game.")
        
        win = False
        
        for i in range(3): # check rows
            if self.board_array[i][0] == "":
                continue
            
            if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                win = True
                break
                
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] == "":
                    continue
                
                if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                    win = True
                    break
                    
        if not win:
            if self.board_array[1][1] != "": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        
        if not win:
            if self.turn == "X": 
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")
        
    def __str__(self) -> str:
        board = ""
        
        for r in range(3):
            line = ""
            
            for c in range(len(self.board_array[r])):
                line += f" {self.board_array[r][c] or " "} "
                
                #add vertical border if not last col
                if c != 2:
                    line += "|"
                    
            board += f"{line}\n"
            
            #add horizontal border if not last row
            if r != 2:
                board += "-----------\n"
                
        return board
        
board = Board()

while True:
    game_over, desc = board.whats_next()
    
    if game_over:
        print("=============")
        print(board)
        print("=============")
        print(desc)
        print("=============")
        break
    
    print(desc)
    print("=============")
    print(board)
    print("=============")
    print(Board.valid_moves)
    print("=============")
    next_move = input(f"Pick a move for {board.turn}: ")
    print("=============")
    
    try:
        print(f"{board.turn} chose the {next_move}")
        board.move(next_move)
    except TictactoeException as ttt_error:
        print(ttt_error.message)