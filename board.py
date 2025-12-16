#Will contain the board used for tic-tac-toe
import math
import random

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
                return False
            else:
                self.__grid[y_cord][x_cord] = player
                self.__free_spaces -= 1
                return True
        else:
            print("Cannot make any more moves")
            return False

    #Allows the program to undo moves so that it can test out many different
    # options in the mini-max algorithm 
    def undo_move(self, x_cord, y_cord):
        if self.__grid[y_cord][x_cord] == '-':
            print("No symbol on that space")
            return False
        else:
            self.__grid[y_cord][x_cord] = '-'
            self.__free_spaces += 1
            return True

    #Will determine if the game has ended or not
    def game_over(self):
        if self.__free_spaces == 0 or self.who_won() != '-':
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
        
    #Creates a list of actions that can be made from the current board state
    def actions(self):
        output = []
        for y in range(3):
            for x in range(3):
                if self.__grid[y][x] == '-':
                    output.append((x, y))
        return output

    #Defines how valuable the end state of the board is
    def utility(self):
        if self.who_won() == 'X':
            return 10
        elif self.who_won() == 'O':
            return -10
        else:
            return 0
        
    #The algorithm which determines what move the computer makes. How it works is
    #by having the computer make the most optimal move based on its own predictions
    #of what the most optimal move its opponent would make
    def min_max(self, depth, maximizing_player):
        #base case where the game ends or the algorithm reaches its maximum depth
        if self.game_over() or depth <= 0:
            return self.utility()
        
        #The computer will try to maximize its own score by checking every available
        #move and picking the most valuable one
        if maximizing_player:
            max_score = -math.inf
            for action in self.actions():
                self.make_move(action[0], action[1], 'X')
                val = self.min_max(depth - 1, False)
                self.undo_move(action[0], action[1])
                max_score = max(max_score, val)
            return max_score
        
        #The computer will simulate the opponents move by having them make the move
        #with the lowest value
        else:
            min_score = math.inf
            for action in self.actions():
                self.make_move(action[0], action[1], 'O')
                val = self.min_max(depth - 1, True)
                self.undo_move(action[0], action[1])
                min_score = min(min_score, val)
            return min_score

    #This method will call the min-max algorithm above for every move the computer can
    #make to see which move is the most optimal.
    #Code gotten from: https://www.datacamp.com/tutorial/minimax-algorithm-for-ai-in-python
    def best_move(self):
        best_score = -math.inf
        best_move = None

        #Tests every possible move to make to see which is the most optimal
        for action in self.actions():
            self.make_move(action[0], action[1], 'X')
            new_score = self.min_max(9, False)
            self.undo_move(action[0], action[1])
            #print(new_score)
            if new_score > best_score:
                #print('Test')
                best_score = new_score
                best_move = action

        return best_move

    #Will simulate a game by having one player make the most optimal moves,
    #and the other make random moves
    def play_game(self):
        computers_turn = True

        while self.game_over() == False:
            if computers_turn:
                move = self.best_move()
                self.make_move(move[0], move[1], 'X')
            else:
                move = random.choice(self.actions())
                self.make_move(move[0], move[1], 'O')

            computers_turn = not computers_turn

        self.print_out()
        print(self.who_won(), ' Wins!')
        return 0