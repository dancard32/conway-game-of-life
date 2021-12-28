import random

def genSpaceships(dat, i,j):
    probability = random.randint(16, 20)

    
    # Glider 1 - 
    if probability == 0:
        dat[i,j] = 1
        dat[i+1,j] = 1
        dat[i-1,j+1] = 1
        dat[i+1,j+1] = 1
        dat[i,j-1] = 1
    elif probability == 1:
        # Glider 2
        dat[i,j] = 1
        dat[i,j+1] = 1
        dat[i+1,j-1] = 1
        dat[i+1,j+1] = 1
        dat[i-1,j] = 1
    
    elif probability == 18:
        # LWSS 1
        dat[i-1,j] = 1
        dat[i-2,j] = 1
        dat[i+1,j] = 1
        dat[i+2,j] = 1

        dat[i,j-1] = 1
        dat[i-1,j-1] = 1
        dat[i-2,j-1] = 1
        dat[i+1,j-1] = 1

        dat[i,j-2] = 1
        dat[i-1,j-2] = 1

        dat[i,j+1] = 1
        dat[i+1,j+1] = 1
        
    elif probability == 19:
        # LWSS 1
        dat[i,j-1] = 1
        dat[i,j-2] = 1
        dat[i,j+1] = 1
        dat[i,j+2] = 1

        dat[i-1,j] = 1
        dat[i-1,j-1] = 1
        dat[i-1,j-2] = 1
        dat[i-1,j+1] = 1

        dat[i-2,j] = 1
        dat[i-2,j-1] = 1

        dat[i+1,j] = 1
        dat[i+1,j+1] = 1

    return dat