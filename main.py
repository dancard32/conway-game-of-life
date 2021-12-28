from numpy.core.numeric import identity
from spaceships import genSpaceships
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import imageio
from PIL import Image 



from Game import genPattern, gol

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def plot_state(x,y,vals, colormap, iteration):
    plt.clf()
    plt.pcolormesh(x,y, vals, cmap=colormap)
    if colormap == 'gist_yarg':
        colormap = 'gist\_yarg'
    elif colormap == 'gist_gray':
        colormap = 'gist\_gray'
    elif colormap ==  'gist_heat':
        colormap = 'gist\_heat'
    elif colormap ==  'twilight_shifted':
        colormap = 'twilight\_shifted'
    elif colormap == 'gist_earth':
        colormap = 'gist\_earth'
    elif colormap ==   'gist_stern':
        colormap = 'gist\_stern'
    elif colormap ==  'gist_rainbow':
        colormap = 'gist\_rainbow'
    elif colormap ==  'nipy_spectral':
        colormap = 'nipy\_spectral'
    elif colormap ==  'gist_ncar':
        colormap = 'gist\_ncar'
    plt.title(colormap + ' Iteration ' + '{:.0f}'.format(iteration), fontsize=14)
    plt.clim(-1,1)
    plt.axis('off')
    plt.axis('equal')
    plt.draw()
    plt.pause(0.01)

def generateRandom(saves, cmap, gifout, weight_True, radial):
    size_mat = 25

    if radial:
        xlin = np.linspace(-5*8, 5*8, size_mat*8); 
    else:
        xlin = np.linspace(0, 2*5*8, size_mat*8); 
    
    ylin = xlin.copy()
    xlin, ylin = np.meshgrid(xlin, ylin)
    r = np.sqrt(xlin**2 + ylin**2)
    dat = xlin*0

    
    """
    for i in range(1, size_mat):
        for j in range(1,size_mat):
            dat = genPattern(dat, i*8,j*8)
    """

    # Generate random initial conditions
    dat = np.random.randint(2, size=(8*size_mat,8*size_mat))

    num_iters = 251
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
        

        identifier = ''
        if weight_True:
            identifier += '_weighted'
        if radial:
            identifier += '_rad'
            
        kargs = { 'duration': 0.00000001 }
        imageio.mimsave('savedGIFS/' + cmap + identifier + gifout + '.gif', images, 'GIF', **kargs)

def ConwayImages(saves, fid, ext, colormap):

        dat = Image.open('Figrep/' + fid + ext)
        dat = dat.convert('1')
        dat = np.flipud(np.array(dat))
        

        xlin = np.arange(dat.shape[0])
        ylin = np.arange(dat.shape[1])
        xlin, ylin = np.meshgrid(ylin, xlin)
        

        num_iters = 25
        for i in range(num_iters):
            print('Iteration %3d'%i)
            
            weights = np.ones((dat.shape[0], dat.shape[1]))

            if saves == True:
                plot_state(xlin, ylin, dat*weights, colormap, i)
                plt.savefig('out/out' + str(i) + '.png', bbox_inches='tight')
            dat = gol(dat)

        if saves:
            images = []
            for iter in range(num_iters):
                images.append(imageio.imread('out/out' + str(int(iter))+ '.png'))
                
            kargs = { 'duration': 0.00000001 }
            imageio.mimsave('FigGIF/'+fid + '.gif', images, 'GIF', **kargs)
def main():

    runSimulations = False
    if runSimulations:
        maplist = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn', 'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper', 'PiYG', 'PRGn', 'BrBG', 'PuOr','RdGy', 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic', 'twilight', 'twilight_shifted', 'hsv', 'Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c', 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral', 'gist_ncar']

        """
        Runtime for a single gif ~5min (While drawing and printing figure)
        If just saving figures ~1min

        Total runtime of ~830min or ~14hrs
        """
        for k in maplist:
            generateRandom(True, k, '', True, True)
            generateRandom(True, k, '', True, False)

            for i in range(3):
                generateRandom(True, k, str(i), False, False)

    loadimages = True
    if loadimages:
        #ConwayImages(True, 'monaLisa', '.jpeg')
        #ConwayImages(True, 'starry_night', '.jpeg')
        ConwayImages(True, 'ethereum', '.jpeg', 'jet')
    
    

if __name__ == "__main__":
    main()


    