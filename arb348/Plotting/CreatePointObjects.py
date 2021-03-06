'''
Created on Apr 11, 2015
@author: Adam Biesenbach
'''

from shapely.prepared import prep
from shapely.geometry import Point, MultiPoint, MultiPolygon
import pandas as pd

def CreatePointObjects(BasemapTemplate, MapData, ComplaintData):
    ''' Here we create a community geometry object from the combined community polygons.  
    We've done this to speed up membership checking. We perform 
    the check by creating a mutipolygon from map_points, then filtering using 
    the contains() method, which returns all points that are contains within 
    community_poygons. The results is a pandas series returning NYCPoints, which we'll use to make out maps. 
    '''
    
    # Create Point objects (in a pandas Series) in map coordinates from our DataFrame longitude and latitude values.
    # Note that the zip function here aggregates the long/lat data for each observation in our compliant data. 
    # The purpose of this code is to convert our latitude and longitude into Basemap cartesian map coordinates 
    
    MapPoints = pd.Series([Point(BasemapTemplate(MapX, MapY)) for MapX, MapY in zip(ComplaintData['Longitude'], ComplaintData['Latitude'])])
        
    # Creates a MultiPoint object from the list of lat/long values from above. 
    
    ComplaintPoints = MultiPoint(list(MapPoints.values))
    
    #  Use the prep method to give this MultiPolygon object (created from the earlier DataFrame of complaint locations), so that it 
    #  has the 'contains' method, which we'll use in the next step. 
    
    CommunityPolygon = prep(MultiPolygon(list(MapData['poly'].values)))
    
    # calculate points that fall within the community boundaries. Here NYCPoints 
    # is a list containing Point objects of all the complaint points contained in 
    # the community polygons.
    
    NYCPoints = filter(CommunityPolygon.contains, ComplaintPoints)
    
    return (NYCPoints)
