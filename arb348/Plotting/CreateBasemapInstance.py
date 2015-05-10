'''
A module to create the basemap instance, which reads in a NYC Shapefile, 
and creates the map output used in later functions. 

Created on Apr 11, 2015
@author: Adam Biesenbach
'''

from mpl_toolkits.basemap import Basemap
import pandas as pd
import fiona
from itertools import chain
from shapely.geometry import Polygon


def BasemapInstance():              
    """ First we open our NYC shapefile, in order to set up our main basemap. Here, we (1) extract the boundaries of the map and (2)
    calculate the extent of the map. Note that I had to 'correct'the original nycd.shp file so that the coordinate system was in 
    degrees rather that feet."""
    
    # Open the NYC shapefile.     
    shp = fiona.open('data/nycd_corrected.shp')
   
    # Save the bounds of the map.
    bds = shp.bounds
    shp.close()  
        
    # Create a list of the map's coordinates. Note that the chain method 
    # returns elements from the first iterable until it is exhausted, then 
    # proceeds to the next iterable, until all of the iterables are exhausted. 
    
    ll = (bds[0], bds[1])
    ur = (bds[2], bds[3])
     
    Coordinates = list(chain(ll, ur))
    extra = 0.01
    width, height = Coordinates[2] - Coordinates[0], Coordinates[3] - Coordinates[1]
        
    """ At this point we're ready to create our basemap instance. This is what will be used to 
        plot our maps on. 
        
        The map used here uses the transverse mercator projection, which apparently exhibits less
        distortion over areas with small east-west distances. This projection requires us to specify 
        a central longitude and latitude. For NYC, I've set this to: -74. and 41.
        
        Here are the other inputs:
        projection: Map projection to use. Here we use the transverse mercator.
        ellps: string describing ellipsoid.
        llcrnrlon: longitude of lower left hand corner of the desired map domain (degrees).
        llcrnrlat: latitude of lower left hand corner of the desired map domain (degrees).
        urcrnrlon: longitude of upper right hand corner of the desired map domain (degrees).
        urcrnrlat: latitude of upper right hand corner of the desired map domain (degrees).
        lat_ts: latitude of true scale. 
        resolution: resolution of boundary database to use. Here (i) is intermediate.
        supress_ticks: suppress automatic drawing of axis ticks and labels in map projection coordinates.  
    """
    BasemapTemplate = Basemap(
        projection='tmerc',
        ellps = 'WGS84',
        lon_0 = -74.,
        lat_0 = 41.,
        llcrnrlon=Coordinates[0] - extra * width,
        llcrnrlat=Coordinates[1] - extra + 0.01 * height,
        urcrnrlon=Coordinates[2] + extra * width,
        urcrnrlat=Coordinates[3] + extra + 0.01 * height,
        lat_ts=0,
        resolution='i',
        suppress_ticks=True)
    
    # Use the basemap class we've just  created and read our NYC data on top of it.
    
    BasemapTemplate.readshapefile(
        'data/nycd_corrected',
        'nyc')    

    """set up a DataFrame containing information about our map. We create a new series 
        in our DataFrame called 'poly', which contains a Polygon object for each neighborhood
        in the shapefile. We also create two more series in this DataFrame called 'area_m' and 
        'area_km' that contain the areas in square meters and square kilometers.  We'll use these later
        to come up with the density values for the choropleth chart.
    """
    MapData = pd.DataFrame({
        'poly': [Polygon(xy) for xy in BasemapTemplate.nyc]})
    MapData['area_m'] = MapData['poly'].map(lambda x: x.area)
    MapData['area_km'] = MapData['area_m'] / 100000
    
    return (BasemapTemplate, MapData, Coordinates)
    