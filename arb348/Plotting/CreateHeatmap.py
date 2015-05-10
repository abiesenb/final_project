'''
This module creates the heatmap plots of the user given complaint type.

Created on Apr 11, 2015
@author: Adam Biesenbach
'''

import matplotlib.pyplot as plt
from descartes import PolygonPatch
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from Plotting.MappingFunctions import ColorBarIndex
import pandas as pd

def Createheatmap(m, breaks, MapData, jenksLabels, Coordinates, ComplaintChoice, FirstDate, LastDate):
    """ Create the heatmap charts. This module saves the chart as a png file. """

    CHFig = plt.figure()
    
    # use a blue color ramp - we'll be converting it to a map using cmap()
    cmap = plt.get_cmap('Blues')
    
    # draw NYC neighborhoods with grey (given by the hex number #555555) outlines.
    MapData['patches'] = MapData['poly'].map(lambda polys: PolygonPatch(polys, ec='#555555', lw=.2, alpha=1., zorder=4))
    
    
    PC = PatchCollection(MapData['patches'], match_original=True)  
    # impose our color map onto the patch collection.
    norm = Normalize()
    PC.set_facecolor(cmap(norm(MapData['jenks_bins'].values)))
    
    Axis = CHFig.add_subplot(111, axisbg='w', frame_on=False)
    Axis.add_collection(PC)

    # Provide some facts about classification method and where the data came from. 
    Axis.text(
        1.03, 0,
        'Classification method: natural breaks\n Contains 311 Complaint data. $\copyright$ 311 data from: https://nycopendata.socrata.com/',
        ha='right', va='bottom',
        size=5,
        color='#555555',
        transform=Axis.transAxes)
    
    # Add a color bar
    ColorBar = ColorBarIndex(ncolors=len(jenksLabels), cmap=cmap, shrink=0.5, labels=jenksLabels)
    ColorBar.ax.tick_params(labelsize=6)
    
    # Add a title
    plt.title("Densities of Complaint type: {0} \n  Date Range: {1} to {2}".format(ComplaintChoice, FirstDate, LastDate))
 
    # Draw a map scale.
    m.drawmapscale(
        Coordinates[0] + 0.08, Coordinates[1] + 0.015,
        Coordinates[0], Coordinates[1],
        10.,
        barstyle='fancy', labelstyle='simple',
        fillcolor1='w', fillcolor2='#555555',
        # #555555 refers to the gray color. 
        fontcolor='#555555',
        zorder=5)
    
    CHFig.set_size_inches(7.22, 5.25)
    title = 'Output/Heatmap_' + str(ComplaintChoice)+ "_" + str(pd.to_datetime(FirstDate).date()) + "_" + str(pd.to_datetime(LastDate).date())  + '.png'
    plt.savefig(title, dpi=100, alpha=True)
    plt.close()