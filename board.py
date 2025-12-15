#Will contain the board used for tic-tac-toe

class Board:
    def __init__(self):
        #Creates the grid that will be used as the board
        self.__grid = [['-' for i in range(3)] for j in range(3)]
        self.__free_spaces = 9

    #Allows the user to see the current state of the game
    def print_out(self):
        for row in self.__grid:
            print(row)

    #Allows a player to place their symbol on the board
    def make_move(self, x_cord, y_cord, player):
        if self.__free_spaces > 0:
            if self.__grid[y_cord][x_cord] != '-':
                print("Cannot place a symbol there")
            else:
                self.__grid[y_cord][x_cord] = player
                self.__free_spaces -= 1
        else:
            print("Cannot make any more moves")

    #Will determine if the game has ended or not
    def game_over(self):
        if self.__free_spaces == 0:
            return True
        else:
            return False
        
    #Will check to see if any of the rows have three in a row
    def __check_rows(self):
        for row in self.__grid:
            if row[0] == row[1] == row[2] and row[0] != '-':
                return row[0]
            
        #If there is no winner, then return '-
        return '-'
    
    #Will check to see if any of the columns have three in a row
    def __check_columns(self):
        for x in range(3):
            if self.__grid[0][x] == self.__grid[1][x] == self.__grid[2][x] and self.__grid[0][x] != '-':
                return self.__grid[0][x]
            
        #If there is no winner, then return '-
        return '-'
    
    #Will check to see if either of the diagonals have three in a row
    def __check_diagonals(self):
        if self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2] and self.__grid[0][0] != '-':
            return self.__grid[0][0]
        elif self.__grid[0][2] == self.__grid[1][1] == self.__grid[2][0] and self.__grid[0][2] != '-':
            return self.__grid[0][0]
        else:
            #If there is no winner, then return '-
            return '-'
        
    #Will determine if there is a winner, and if so who it is
    def who_won(self):
        rows = self.__check_rows()
        columns = self.__check_columns()
        diagonals = self.__check_diagonals()

        if rows != '-':
            return rows
        elif columns != '-':
            return columns
        elif diagonals != '-':
            return diagonals
        else:
            return '-'

        