# Conways's Game of Life
# Hosted on @Toblobs GitHub

import random
from time import sleep

from __init__ import __version__, __snap__
    
class Cell:

    def __init__(self, state, row, column, out_of_bounds = False):

        self.state = state
        self.row = row
        self.column = column

        self.out_of_bounds = out_of_bounds

class Board:

    def __init__(self, length, width, torodial):

        self.length = length
        self.width = width
        self.torodial = torodial

        self.cell_list = [] # 2D List

    def initialise_board(self):

        self.fill_board()

    def clear_board(self):

        for x in range(self.width):
            
            self.cell_list.append([])
            for y in range(self.length):
                self.cell_list[x].append(Cell(state = 'Dead', row = x, column = y))

    def fill_board(self):
        
        for x in range(self.width):
            
            self.cell_list.append([])
            for y in range(self.length):

                if random.randint(0, 100) <= 20:
                    self.cell_list[x].append(Cell(state = 'Alive', row = x, column = y))
                else:
                    self.cell_list[x].append(Cell(state = 'Dead', row = x, column = y))

    def __str__(self):
        
        for x in range(self.width):
            for y in range(self.length):
                if self.cell_list[x][y].state == 'Alive':
                    print(f'|⬜', end = '')
                else:
                    print(f'|⬛', end = '')

                    
                #print(f'| {self.cell_list[x][y].state[0]} {x}/{y}', end = '')

            print('|\n')
            print('━' * 40)

        print('\n'*10)

        return ''

    def get_cell(self, row, column):

        try:
            
            return self.cell_list[row][column]

        except:

            return Cell(state = 'Dead', row = row, column = column, out_of_bounds = True)
        
    def tick(self):

        for x in range(self.width):
            for y in range(self.length):

                this_cell = self.cell_list[x][y]

                row = this_cell.row
                column = this_cell.column

                neighbours = [self.get_cell(row - 1, column - 1),
                                self.get_cell(row - 1, column + 0),
                                self.get_cell(row - 1, column + 1),
                                self.get_cell(row + 0, column - 1),
                                self.get_cell(row + 0, column + 1),
                                self.get_cell(row + 1, column - 1),
                                self.get_cell(row + 1, column + 0),
                                self.get_cell(row + 1, column + 1)]

                # sprint(neighbours)

                # Handling rules
                state_neighbours = [n.state for n in neighbours]
                alive_count = state_neighbours.count('Alive')

                # Handling alive cells

                if this_cell.state == 'Alive' and this_cell.out_of_bounds == False:

                    if alive_count < 2:
                        this_cell.state = 'Dead'

                    if alive_count > 3:
                        this_cell.state = 'Dead'

                # Handling dead cells
                else:

                    if alive_count == 3:
                        this_cell.state = 'Alive'
                    

    
            
    

def conways_game_of_life():

    from time import sleep

    # Important settings
    
    BOARD_LENGTH = 10
    BOARD_WIDTH = 10
    
    TORODIAL = False # If the board wraps around itself
    SIMULATION_LENGTH = -1 # -1: infinite, else is amount of steps
    STEP = 0 # current time step

    SLEEP_LENGTH = 5 # How long the program waits for / step

    # Board initialisation
    board = Board(BOARD_LENGTH, BOARD_WIDTH, TORODIAL)
    board.initialise_board()

    # Lambda function to return the column in any 2D list
    # return_col = lambda col, lst: [row[col] for row in lst]

    print(f'Game Of Life v{__version__}')
    print()

    while True:

        board.tick()
        print(board)

        # Game Tick

        if SIMULATION_LENGTH == -1: # Infinite
            pass

        if SIMULATION_LENGTH == 0: # Finite, we ran out of time, break loop
            break

        else:
            SIMULATION_LENGTH == SIMULATION_LENGTH -1  #  Finite, time runs down by one

        STEP = STEP + 1
    
        sleep(SLEEP_LENGTH)
        

conways_game_of_life()


                
        
