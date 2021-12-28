import random

def genOscillators(dat, i, j):
    probability = random.randint(0, 9)
    
    # Blinker - Horizontal
    if probability == 0:
        dat[i,j] = 1
        dat[i-1,j] = 1
        dat[i+1,j] = 1

    # Blinker - Vertical
    elif probability == 1:
        dat[i,j] = 1
        dat[i,j+1] = 1
        dat[i,j-1] = 1

    # Toad 1 - Vertical
    elif probability == 2:
        dat[i,j] = 1
        dat[i-1,j] = 1
        dat[i+1,j] = 1
        dat[i,j-1] = 1
        dat[i-1,j-1] = 1
        dat[i-2,j-1] = 1
    
    # Toad 1 - Horizontal
    elif probability == 3:
        dat[i,j] = 1
        dat[i,j-1] = 1
        dat[i,j+1] = 1
        dat[i-1,j] = 1
        dat[i-1,j-1] = 1
        dat[i-1,j-2] = 1

    # Toad 2 - Vertical
    elif probability == 4:    
        dat[i,j+1] = 1
        dat[i+1,j] = 1
        dat[i+1,j-1] = 1
        dat[i-2,j] = 1
        dat[i-2,j-1] = 1
        dat[i-1,j-2] = 1

    # Toad 2 - Horizontal
    elif probability == 5:    
        dat[i+1,j] = 1
        dat[i,j+1] = 1
        dat[i-1,j+1] = 1
        dat[i,j-2] = 1
        dat[i-1,j-2] = 1
        dat[i-2,j-1] = 1

    # Beacon 1 - Vertical
    elif probability == 6:
        dat[i-1,j] = 1
        dat[i-2,j] = 1
        dat[i-1,j+1] = 1
        dat[i-2,j+1] = 1
        dat[i,j-1] = 1
        dat[i,j-2] = 1
        dat[i+1,j-1] = 1
        dat[i+1,j-2] = 1

    # Beacon 2 - Vertical
    elif probability == 7:
        dat[i-2,j] = 1
        dat[i-1,j+1] = 1
        dat[i-2,j+1] = 1
        dat[i,j-2] = 1
        dat[i+1,j-1] = 1
        dat[i+1,j-2] = 1

    # Beacon 1 - Horizontal
    elif probability == 8:
        dat[i,j-1] = 1
        dat[i,j-2] = 1
        dat[i+1,j-1] = 1
        dat[i+1,j-2] = 1
        dat[i-1,j] = 1
        dat[i-2,j] = 1
        dat[i-1,j+1] = 1
        dat[i-2,j+1] = 1

    # Beacon 2 - Horizontal
    elif probability == 9:
        dat[i,j-2] = 1
        dat[i+1,j-1] = 1
        dat[i+1,j-2] = 1
        dat[i-2,j] = 1
        dat[i-1,j+1] = 1
        dat[i-2,j+1] = 1

    return dat