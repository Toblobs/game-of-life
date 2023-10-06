# Conways's Game of Life
# Hosted on @Toblobs GitHub

import random
from time import sleep
import threading

from __init__ import __version__, __snap__, get_package

# Import packages
import tkinter as tk

get_package('numpy')
import numpy

class TkinterGrid:

    def __init__(self, row_len, col_len):

        self.window = None
        
        self.row_len = row_len
        self.col_len = col_len

    def begin(self, a):

        self.window = tk.Tk()
        self.window.title(f'Game Of Life v{__version__} - {__snap__}')

        for x in range(self.row_len):
            
            for y in range(self.col_len):
                
                frame = tk.Frame(
                    master = self.window,
                    relief = tk.RAISED,
                    borderwidth = 1
                )
                
                
                frame.grid(row = x, column = y)
                label = tk.Label(master = frame, text = '⬛')
                label.pack()

        self.window.mainloop()

    def paint_cells(self, cells):

        for x in range(self.row_len):

            for y in range(self.col_len):

                this_cell = cells[x][y]

                if not (this_cell.state == this_cell.previous_state):

                    frame = tk.Frame(
                        master = self.window,
                        relief = tk.RAISED,
                        borderwidth = 1
                    )

                    frame.grid(row = x, column = y)
                    label = tk.Label(master = frame, text = this_cell.state)
                    label.pack()

                else:

                    pass 
        
class Cell:

    def __init__(self, state, row, column, out_of_bounds = False):

        self.state = state
        self.row = row
        self.column = column

        self.out_of_bounds = out_of_bounds

        self.previous_state = None

    def change_state(self, sta):

        self.previous_state = self.state
        self.state = sta


class Board:

    def __init__(self, length, width, torodial):

        self.length = length
        self.width = width
        self.torodial = torodial

        self.cell_list = [] # 2D List

    def initialise_board(self, brd = None):

        self.fill_board(brd)

    def clear_board(self):

        for x in range(self.width):
            
            self.cell_list.append([])
            for y in range(self.length):
                self.cell_list[x].append(Cell(state = '⬛', row = x, column = y))

    def fill_board(self, board = None):

        for x in range(self.width):
            
            self.cell_list.append([])
            for y in range(self.length):

                if board == None:

                    if random.randint(0, 100) <= 10:
                        self.cell_list[x].append(Cell(state = '⬜', row = x, column = y))
                    else:
                        self.cell_list[x].append(Cell(state = '⬛', row = x, column = y))

                else:
                    self.cell_list[x].append(Cell(state = board[x][y], row = x, column = y))

    def print(self, tkgrid):
                
        tkgrid.paint_cells(self.cell_list)

    def get_cell(self, row, column):

        try:
            
            return self.cell_list[row][column]

        except:

            return Cell(state = '⬛', row = row, column = column, out_of_bounds = True)
        
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
                alive_count = state_neighbours.count('⬜')

                # Handling alive cells

                if this_cell.state == '⬜' and this_cell.out_of_bounds == False:

                    if alive_count < 2:
                        this_cell.change_state('⬛')

                    if alive_count > 3:
                        this_cell.change_state('⬛')

                # Handling dead cells
                else:

                    if alive_count == 3:
                        this_cell.change_state('⬜')
                    

    
            
    

def conways_game_of_life():

    from time import sleep

    # Important settings
    
    BOARD_LENGTH = 20
    BOARD_WIDTH = 20

    CELL_COORDS = [(6, 3), (6, 4), (6, 5)]
    
    TORODIAL = False # If the board wraps around itself
    SIMULATION_LENGTH = -1 # -1: infinite, else is amount of steps
    STEP = 0 # current time step

    SLEEP_LENGTH = 1 # How long the program waits for / step

    # Board initialisation
    board = Board(BOARD_LENGTH, BOARD_WIDTH, TORODIAL)

    #my_brd = []

    #for x in range(BOARD_LENGTH):
    #    my_brd.append([])
        
    #    for y in range(BOARD_WIDTH):
    #        if (x, y) in CELL_COORDS:
    #           my_brd[x].append('⬜')
    #        else:
    #            my_brd[x].append('⬛')
            
    board.initialise_board()

    # Lambda function to return the column in any 2D list
    # return_col = lambda col, lst: [row[col] for row in lst]

    grd = TkinterGrid(BOARD_LENGTH, BOARD_WIDTH)
    
    t = threading.Thread(target = grd.begin, args = (1,))
    t.start()


    while True:

        board.tick()
        
        # Game Tick

        if SIMULATION_LENGTH == -1: # Infinite
            pass

        if SIMULATION_LENGTH == 0: # Finite, we ran out of time, break loop
            break

        else:
            SIMULATION_LENGTH == SIMULATION_LENGTH -1  #  Finite, time runs down by one

        STEP = STEP + 1
    
        sleep(SLEEP_LENGTH)

        board.print(grd)
        

conways_game_of_life()


                
        
