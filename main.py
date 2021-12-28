import matplotlib.pyplot as plt
import numpy as np
import imageio
import json
import os

from PIL import Image 
from Game import genPattern, gol
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    Sets up default text interpreter (LaTeX
    Comment out these two lines if LaTeX is not locally installed
"""
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def plot_state(x,y,vals, colormap, iteration):
    plt.clf()
    plt.pcolormesh(x,y, vals, cmap=colormap)
    plt.title(colormap.replace('_','\_') +' Iteration '+'{:.0f}'.format(iteration), fontsize=14)
    plt.clim(-1,1)
    plt.axis('off')
    plt.axis('equal')
    plt.draw()
    plt.pause(0.01)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def generateRandom(saves, cmap, gifout, weight_True, radial):
    size_mat = 25

    if radial: xlin = np.linspace(-5*8, 5*8, size_mat*8); 
    else: xlin = np.linspace(0, 2*5*8, size_mat*8); 
    
    ylin = xlin.copy()
    xlin, ylin = np.meshgrid(xlin, ylin)
    r = np.sqrt(xlin**2 + ylin**2)
    dat = xlin*0

    """
        Un-comment this block and re-comment dat = np.random... to start with patterns
        that have been identified on the Wiki page (oscillators, ships, etc.)
    """

    """
    for i in range(1, size_mat):
        for j in range(1,size_mat):
            dat = genPattern(dat, i*8,j*8)    
    """

    # Un-comment to generate random initial conditions
    dat = np.random.randint(2, size=(8*size_mat,8*size_mat))

    # Increase/decrease the number of iterations 
    num_iters = 100
    for i in range(num_iters):
        print('Iteration %3d'%i)
        if weight_True:
            weights =  np.cos(r - i)
        else:
            weights = np.ones((size_mat*8, size_mat*8))

        if saves == True:
            plot_state(xlin, ylin, dat*weights, cmap, i)
            plt.savefig('out/out' + str(i) + '.png', bbox_inches='tight')
        dat = gol(dat)

    if saves:
        images = []
        for iter in range(num_iters):
            images.append(imageio.imread('out/out' + str(int(iter))+ '.png'))
            os.remove('out/out' + str(int(iter))+ '.png')
        
        identifier = ''
        if weight_True: identifier += '_weighted'
        if radial: identifier += '_rad'
            
        kargs = { 'duration': 0.001 }
        imageio.mimsave('savedGIFS/' + cmap + identifier + gifout + '.gif', images, 'GIF', **kargs)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ConwayImages(saves, fid, colormap):
    # Load an image and gray-scale it as the initial condition
    dat = Image.open('Figrep/' + fid)
    dat = dat.convert('1')
    dat = np.flipud(np.array(dat))
    
    # Set-up initial matrix
    xlin = np.arange(dat.shape[0])
    ylin = np.arange(dat.shape[1])
    xlin, ylin = np.meshgrid(ylin, xlin)
    
    # Loaded images are large, and take longer to run - use lower iterations for faster run times
    num_iters = 25
    for i in range(num_iters):
        print('Iteration %3d'%i)    # Print out current iteration
        weights = np.ones((dat.shape[0], dat.shape[1]))

        if saves == True:
            plot_state(xlin, ylin, dat*weights, colormap, i)
            plt.savefig('out/out' + str(i) + '.png', bbox_inches='tight')
        dat = gol(dat)
    if saves:
        images = []
        for iter in range(num_iters):
            images.append(imageio.imread('out/out' + str(int(iter))+ '.png'))
            os.remove('out/out' + str(int(iter))+ '.png')
            
        kargs = { 'duration': 0.01 }    # Set the duration of each frame
        imageio.mimsave('FigGIF/'+fid.rsplit('.')[0] + '.gif', images, 'GIF', **kargs)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main(maplist, images):
    
    maplist = ['gist_earth']    # Comment this line to run the entire cmap dictionary found in maps.json

    """
    Runtime for a single gif ~5min (While drawing and printing figure)
    Total runtime for all colormaps is ~830min or ~14hrs
    """
    for k in maplist:
        # Save figures, cmap, gif iteration, weighted (color changes), radial weight
        generateRandom(True, k, '', True, True)
        generateRandom(True, k, '', True, False)

        for i in range(3):
            generateRandom(True, k, str(i), False, False)

    """ Loop through the passed in image files """
    for i in images: ConwayImages(True, i, 'jet')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    # Load mapslist from maps.json dictionary, and add photos from "Figrep/" to input into GOL
    fid = open("maps.json"); mapslist = json.load(fid); fid.close()
    image_names = ['ethereum.jpeg']

    # Run main script
    main(mapslist['maps'], image_names)
