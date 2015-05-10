'''
This module creates the scatter plots of the user given complaint type.

Created on Apr 11, 2015
@author: Adam Biesenbach
'''

import matplotlib.pyplot as plt
from descartes import PolygonPatch
from matplotlib.collections import PatchCollection
import pandas as pd

def CreateScatterPlot(df_map, nyc_points, m, coords, ComplaintChoice, FirstDate, LastDate):
    '''draw community  patches from polygons.'''
    
    df_map['patches'] = df_map['poly'].map(lambda x: PolygonPatch(
        x,
        fc='#555555',
        ec='#787878', lw=.25, alpha=.9,
        zorder=4))
    
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111, axisbg='w', frame_on=False)
    
    # we don't need to pass points to m() because we calculated using map_points and shapefile polygons
    m.scatter(
        [geom.x for geom in nyc_points],
        [geom.y for geom in nyc_points],
        5, marker='o', lw=.25,
        facecolor='#33ccff', edgecolor='w',
        alpha=0.9, antialiased=True,
        label='Blue Plaque Locations', zorder=3)
    
    # plot boroughs by adding the PatchCollection to the axes instance
    ax.add_collection(PatchCollection(df_map['patches'].values, match_original=True))
    
    # Add a title
    plt.title("Locations of Complaint type: {0} \n  Date Range: {1} to {2}".format(ComplaintChoice, FirstDate, LastDate))

    # copyright and source data info
    ax.text(
        1.03, 0,
        'Total Complaints: %s \nContains 311 Complaint data. $\copyright$ 311 data from: https://nycopendata.socrata.com/' % len(nyc_points),
        ha='right', va='bottom',
        size=7,
        color='#555555',
        transform=ax.transAxes)
    
    # Draw a map scale
    m.drawmapscale(
        coords[0] + 0.03, coords[1] + 0.02,
        coords[0], coords[1],
        10.,
        barstyle='fancy', labelstyle='simple',
        fillcolor1='w', fillcolor2='#555555',
        fontcolor='#555555',
        zorder=5)

    fig.set_size_inches(7.22, 5.25)
    title = 'Output/Scatter_' + str(ComplaintChoice) + "_" + str(pd.to_datetime(FirstDate).date()) + "_" + str(pd.to_datetime(LastDate).date()) + '.png'
    plt.savefig(title, dpi=100, alpha=True)
    