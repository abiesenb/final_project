'''
This module creates the choropleth plots of the user given complaint type.

Created on Apr 11, 2015
@author: Adam Biesenbach
'''

import matplotlib.pyplot as plt
from descartes import PolygonPatch
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from Plotting.MappingFunctions import colorbar_index
import pandas as pd

def CreateChoropleth(m, breaks, df_map, jenks_labels, coords, ComplaintChoice, FirstDate, LastDate):
    """ Create the choropleth charts. This module saves the chart as a png file. """

    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111, axisbg='w', frame_on=False)
    
    # use a blue color ramp - we'll be converting it to a map using cmap()
    cmap = plt.get_cmap('Blues')
    
    # draw NYC neighborhoods with grey outlines.
    df_map['patches'] = df_map['poly'].map(lambda x: PolygonPatch(x, ec='#555555', lw=.2, alpha=1., zorder=4))
    pc = PatchCollection(df_map['patches'], match_original=True)
    
    # impose our color map onto the patch collection.
    norm = Normalize()
    pc.set_facecolor(cmap(norm(df_map['jenks_bins'].values)))
    ax.add_collection(pc)
    
    # Add a color bar
    cb = colorbar_index(ncolors=len(jenks_labels), cmap=cmap, shrink=0.5, labels=jenks_labels)
    cb.ax.tick_params(labelsize=6)
    
    # Add a title
    plt.title("Densities of Complaint type: {0} \n  Date Range: {1} to {2}".format(ComplaintChoice, FirstDate, LastDate))

    # Provide some facts about classification method and where the data came from. 
    ax.text(
        1.03, 0,
        'Classification method: natural breaks\n Contains 311 Complaint data. $\copyright$ 311 data from: https://nycopendata.socrata.com/',
        ha='right', va='bottom',
        size=7,
        color='#555555',
        transform=ax.transAxes)
    
    # Draw a map scale.
    m.drawmapscale(
        coords[0] + 0.08, coords[1] + 0.015,
        coords[0], coords[1],
        10.,
        barstyle='fancy', labelstyle='simple',
        fillcolor1='w', fillcolor2='#555555',
        fontcolor='#555555',
        zorder=5)
    
    fig.set_size_inches(7.22, 5.25)
    title = 'Output/Choropleth_' + str(ComplaintChoice)+ str(pd.to_datetime(FirstDate).date()) + "_" + str(pd.to_datetime(LastDate).date())  + '.png'
    plt.savefig(title, dpi=100, alpha=True)