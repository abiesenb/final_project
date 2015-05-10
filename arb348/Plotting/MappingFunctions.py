'''
These functions make creating the heat map a little easier. 

Created on Apr 11, 2015
@author: Adam Biesenbach
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm


# Convenience functions for working with color ramps and bars. Note that the 
# inclusion of **kwargs allows us to pass an arbitrary number of keyword 
# arguments to the function. 

def ColorBarIndex(ncolors, cmap, labels=None, **kwargs):
    '''This is a convenience function that draws a color bar with correctly aligned labels'''
  
    # Get the colormap from the function below.
    cmap = ColorMap(cmap, ncolors)
    
    # class to support scalar data to RGBA mapping. 
    # The ScalarMappable makes use of data normalization before returning
    # RGBA colors from the given colormap.
    Mapping = cm.ScalarMappable(cmap=cmap)
    
    # Set the image array. 
    Mapping.set_array([])
    
    # set the norm limits for image scaling.
    Mapping.set_clim(-0.5, ncolors+0.5)
    
    # The derived class from the colorbar base class, 
    # for use with images or contour plots.
    colorbar = plt.colorbar(Mapping, **kwargs)
    colorbar.set_ticks(np.linspace(0, ncolors, ncolors))
    colorbar.set_ticklabels(range(ncolors))
    if labels:
        colorbar.set_ticklabels(labels)
    return colorbar

def ColorMap(cmap, NumberOfColors):
    '''Return a discrete colormap from the continuous colormap cmap. The
    cmap argument is the colormap, while the N argument is the number 
    of color we need (in this case, equal to the number of jenks breaks that 
    the program determines. '''
    
    ColorIndex = np.concatenate((np.linspace(0, 1, NumberOfColors), (0., 0., 0., 0.)))
    RGBAColorIndex = cmap(ColorIndex)
    indices = np.linspace(0, 1, NumberOfColors + 1)
    
    ColorDict = {}
    for CIndex, Color in enumerate(('red', 'green', 'blue')):
        ColorDict[Color] = [(indices[i], RGBAColorIndex[i - 1, CIndex], RGBAColorIndex[i, CIndex]) for i in xrange(NumberOfColors + 1)]
    
    # Here we use the LinearSegmentedColormap class to create the new colormap object. 
    return matplotlib.colors.LinearSegmentedColormap(cmap.name + "_%d" % NumberOfColors, ColorDict, 1024)
