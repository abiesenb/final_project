'''
Created on Apr 11, 2015
@author: Adam Biesenbach
'''

import numpy as np 
from shapely.prepared import prep

def SummarizeByCommunity(MapData, NYCPoints):
    """Create some additional columns, containing the number of points in each NYC community, and the density 
    per square meter and square kilometer community. Normalizing allows us to compare communities."""
        
    MapData['count'] = MapData['poly'].map(lambda x: int(len(filter(prep(x).contains, NYCPoints))))
    MapData['density_m'] = MapData['count'] / MapData['area_m']
    MapData['density_km'] = MapData['count'] / MapData['area_km']
    
    # it's easier to work with NaN values when classifying, so replace zeros with NaNs when appropriate.
    MapData.replace(to_replace={'density_m': {0: np.nan}, 'density_km': {0: np.nan}}, inplace=True)
    
    return MapData