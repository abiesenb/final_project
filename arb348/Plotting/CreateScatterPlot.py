'''
This module creates the scatter plots of the user given complaint type.

Created on Apr 11, 2015
@author: Adam Biesenbach
'''

import matplotlib.pyplot as plt
from descartes import PolygonPatch
from matplotlib.collections import PatchCollection
import pandas as pd

def CreateScatterPlot(MapData, NYCPoints, BasemapTemplate, Coordinates, ComplaintChoice, FirstDate, LastDate):
  
    # draw community  patches from polygons.  
    PatchedMapData = DrawCommuninityPatches(MapData)
    
    # Create an instance of the figure class. 
    ScatterFig = plt.figure()
    
    # Add a subplot, where '111' refers 
    # to grid parameters encoded as a single integer. 
    # "111" means "1x1 grid, first subplot". We also set the background
    # color to white.
    
    Axis = ScatterFig.add_subplot(111, axisbg='w', frame_on=False)

    BasemapTemplate.scatter(
        [geom.x for geom in NYCPoints],
        [geom.y for geom in NYCPoints],
        5, marker='o', lw=.25,
        facecolor='#33ccff', edgecolor='w',
        alpha=0.9, antialiased=True,
        label='Locations of Complaints', zorder=3)
        
    # Add a title
    plt.title("Locations of Complaint type: {0} \n  Date Range: {1} to {2}".format(ComplaintChoice, FirstDate, LastDate))

    # plot boroughs by adding the PatchCollection to the axes instance
    Axis.add_collection(PatchCollection(PatchedMapData['patches'].values, match_original=True))
    
    # copyright and source data info
    Axis.text(
        1.03, 0,
        'Total Complaints: %s \nContains 311 Complaint data. $\copyright$ 311 data from: https://nycopendata.socrata.com/' % len(NYCPoints),
        ha='right', va='bottom',
        size=5,
        # This hex number will make the border dark gray.
        color='#555555',
        transform=Axis.transAxes)
    
    # Draw a map scale
    BasemapTemplate.drawmapscale(
        Coordinates[0] + 0.03, Coordinates[1] + 0.02,
        Coordinates[0], Coordinates[1],
        10.,
        barstyle='fancy', labelstyle='simple',
        fillcolor1='w', fillcolor2='#555555',
        fontcolor='#555555',
        zorder=5)

    ScatterFig.set_size_inches(7.22, 5.25)
    
    title = 'Output/Scatter_' + str(ComplaintChoice) + "_" + str(pd.to_datetime(FirstDate).date()) + "_" + str(pd.to_datetime(LastDate).date()) + '.png'
    plt.savefig(title, dpi=100, alpha=True)
    plt.close()


def DrawCommuninityPatches(MapData):  
    '''Draw community  patches from polygons.'''
    MapData['patches'] = MapData['poly'].map(lambda Polys: PolygonPatch(
    Polys,
    # 555555 refers to darker gray.
    fc='#555555',
    # 787878 refers to lighter gray. 
    ec='#787878', lw=.25, alpha=.9,
    zorder=4))
    
    return MapData