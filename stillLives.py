import random

def genStills(dat, i,j):
    probability = random.randint(0, 11)

    # Block
    if probability == 0:    
        dat[i,j] = 1
        dat[i-1,j] = 1
        dat[i,j-1] = 1
        dat[i-1,j-1] = 1

    # Bee-Hive - Vertical
    elif probability == 1:    
        dat[i,j+1] = 1
        dat[i-1,j+1] = 1
        dat[i-2,j] = 1
        dat[i-1,j-1] = 1
        dat[i,j-1] = 1
        dat[i+1,j] = 1

    # Bee-Hive - Horizontal
    elif probability == 2:    
        dat[i+1,j] = 1
        dat[i+1,j-1] = 1
        dat[i,j-2] = 1
        dat[i-1,j-1] = 1
        dat[i-1,j] = 1
        dat[i,j+1] = 1

    # Loaf - Top right
    elif probability == 3:    
        dat[i,j+1] = 1
        dat[i-1,j+1] = 1
        dat[i-2,j] = 1
        dat[i-1,j-1] = 1
        dat[i,j-2] = 1
        dat[i+1,j-1] = 1
        dat[i+1,j] = 1

    # Loaf - Top left
    elif probability == 4:
        dat[i,j+1] = 1
        dat[i+1,j+1] = 1
        dat[i+2,j] = 1
        dat[i+1,j-1] = 1
        dat[i,j-2] = 1
        dat[i-1,j-1] = 1
        dat[i-1,j] = 1

    # Loaf - Bottom right
    elif probability == 5:
        dat[i,j-1] = 1
        dat[i-1,j-1] = 1
        dat[i-2,j] = 1
        dat[i-1,j+1] = 1
        dat[i,j+2] = 1
        dat[i+1,j+1] = 1
        dat[i+1,j] = 1
        
    # Loaf - Bottom left
    elif probability == 6:
        dat[i+1,j+1] = 1
        dat[i+2,j] = 1
        dat[i+1,j-1] = 1
        dat[i,j-1] = 1
        dat[i-1,j] = 1
        dat[i-1,j+1] = 1
        dat[i,j+2] = 1

    # Boat - Top left
    elif probability == 7:
        dat[i+1,j] = 1
        dat[i-1,j] = 1
        dat[i,j-1] = 1
        dat[i,j+1] = 1
        dat[i-1,j+1] = 1

    # Boat - Top right
    elif probability == 8:    
        dat[i+1,j] = 1
        dat[i-1,j] = 1
        dat[i,j-1] = 1
        dat[i,j+1] = 1
        dat[i+1,j+1] = 1

    # Boat - Bottom left
    elif probability == 9:  
        dat[i+1,j] = 1
        dat[i-1,j] = 1
        dat[i,j-1] = 1
        dat[i,j+1] = 1
        dat[i-1,j-1] = 1

    # Boat - Bottom right
    elif probability == 10:
        dat[i+1,j] = 1
        dat[i-1,j] = 1
        dat[i,j-1] = 1
        dat[i,j+1] = 1
        dat[i-1,j+1] = 1

    # Tub
    elif probability == 11:    
        dat[i+1,j] = 1
        dat[i-1,j] = 1
        dat[i,j-1] = 1
        dat[i,j+1] = 1

    return dat