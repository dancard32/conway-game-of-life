import random

from stillLives import genStills
from oscillators import genOscillators
from spaceships import genSpaceships

def genPattern(dat, i, j):
    initial_type = random.randint(0,5)
    
    """
    Generate the patterns in Game of Life as initial start
    """
    if initial_type == 0:
        dat = genStills(dat, i,j)
    elif initial_type == 1:
        dat = genOscillators(dat, i,j)
    elif initial_type > 1 and initial_type < 3:
        dat = genSpaceships(dat, i,j)

    return dat

def gol(vals):
    Nx = vals.shape[0] - 1; Ny = vals.shape[1]-1
    new_vals = 0*vals.copy()
    for j in range(Nx):
        for i in range(Ny):
            num_neighbors = 0

            # Calculate the number of neighbors
            if vals[j%Nx,(i-1)%Ny] == 1:    # Left
                num_neighbors+=1
            if vals[j%Nx,(i+1)%Ny] == 1:    # Right
                num_neighbors+=1
            if vals[(j-1)%Nx,i%Ny] == 1:    # Down
                num_neighbors+=1
            if vals[(j+1)%Nx,i%Ny] == 1:    # Up
                num_neighbors+=1
            if vals[(j+1)%Nx,(i-1)%Ny] == 1:  # Up-Left
                num_neighbors+=1
            if vals[(j+1)%Nx,(i+1)%Ny] == 1:  # Up-Right
                num_neighbors+=1
            if vals[(j-1)%Nx,(i-1)%Ny] == 1:  # Down-Left
                num_neighbors+=1
            if vals[(j-1)%Nx,(i+1)%Ny] == 1:  # Down=Right
                num_neighbors+=1

            # Generate next iteration
            if vals[j,i] == 1 and num_neighbors < 2:
                new_vals[j,i] = 0
            elif vals[j,i] == 1 and num_neighbors == 2:
                new_vals[j,i] = 1
            elif vals[j,i] == 1 and num_neighbors == 3:
                new_vals[j,i] = 1
            elif vals[j,i] == 1 and num_neighbors > 3:
                new_vals[j,i] = 0
            elif vals[j,i] == 0 and num_neighbors == 3:
                new_vals[j,i] = 1
            
    return new_vals