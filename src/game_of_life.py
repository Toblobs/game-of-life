# Conway's Game of Life
# Hosted on @Toblobs GitHub

from __init__ import get_package, __version__, __snap__

get_package('numpy')
get_package('matplotlib')
get_package('argparse')

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

import argparse
 
ALIVE = 245
DEAD = 10
states = [ALIVE, DEAD]
 
def random_grid(size):

    return np.random.choice(states, size * size, p=[0.2, 0.8]).reshape(size, size)

def repaint(frames, img, grid, size):
  
    final_grid = grid.copy()
    for i in range(size):
        for j in range(size):
 
            total = int((grid[i, (j-1)%size] + grid[i, (j+1)%size] +
                         grid[(i-1)%size, j] + grid[(i+1)%size, j] +
                         grid[(i-1)%size, (j-1)%size] + grid[(i-1)%size, (j+1)%size] +
                         grid[(i+1)%size, (j-1)%size] + grid[(i+1)%size, (j+1)%size])/255)

            ## Overcrowding / Overpopulation
            if grid[i, j] == states[0]:
                if (total < 2) or (total > 3):
                    final_grid[i, j] = states[1]

            ## Reproduction  
            else:
                if total == 3:
                    final_grid[i, j] = states[0]
 
    img.set_data(final_grid)
    grid[:] = final_grid[:]
    return img
 
def start():

    ## Constant Definitions
    grid_size = 100
    torodial = True
    f_interval = 50

    grid = np.array([])
    grid = random_grid(grid_size)

    ## Parser for Arguments
    __par = argparse.ArgumentParser(description = f'Game of Life v{__version__}-{__snap__}')
    __par.add_argument('--mov-file', dest = 'movfile', required = False)
    arg = __par.parse_args()
    
    ## Set up MatPlotLib
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')

    ## Animation Function that will repaint every interval
    ani = animation.FuncAnimation(fig, repaint, fargs=(img, grid, grid_size),
                                  frames = 10,
                                  interval = f_interval,
                                  save_count = 50)
    if arg.movfile:
        ani.save(arg.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    print(f'Running Game of Life v{__version__}-{__snap__}')
    plt.show()

start()
