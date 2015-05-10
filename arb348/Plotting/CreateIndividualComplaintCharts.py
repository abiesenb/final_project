'''
This module creates the heatmap, scatter and Borough pie plot for the selected complaint
type and date range. 

Created on May 5, 2015
@author: Adam Biesenbach
'''

from Plotting.CreateBasemapInstance import BasemapInstance
from Plotting.ComputeJenksBreaks import ComputeJenksBreaks
from Plotting.CreateHeatmap import Createheatmap
from Plotting.SummarizeByCommunity import SummarizeByCommunity
from Plotting.CreatePointObjects import CreatePointObjects
from Plotting.CreateScatterPlot import CreateScatterPlot
from Plotting.CreatePiePlots import CreateBoroughPiePlot

def CreateIndividualCharts(ComplaintChoice, ComplaintData, FirstDate, LastDate):

    ''' Create a basemap instance of our NYC shapefile. Returns:
            BasemapTemplate: the basemap instance of our NYC shapefile. 
            MapData: DataFrame containing information about our map.
            Coordinates: The four coordinates for the extent of the map. '''
            
    (BasemapTemplate, MapData, Coordinates) = BasemapInstance()
    
    ''' Create the 'Point objects'. Returns:
         NYCPoints: '''
         
    (NYCPoints) = CreatePointObjects(BasemapTemplate, MapData, ComplaintData)
    
    ''' Create summary values of the number of given complaint type in given district/community. Returns:
        the same DataFrame as before, this time with added summary columns. '''
             
    MapData = SummarizeByCommunity(MapData, NYCPoints)
    
    ''' Generate the Jenks breaks for our heatmap charts. Returns:
            Breaks: the Jenks natural breaks for density.
            MapData: the DataFrame containing our lat/long complaint info.
            JenksLabels: Labels used to label the key on the final heatmap. '''
    
    (Breaks, MapData, JenksLabels) = ComputeJenksBreaks(MapData)
    
    ''' Create the heatmap charts. This module saves the chart as a png file. '''
    try:
        Createheatmap(BasemapTemplate, Breaks, MapData, JenksLabels, Coordinates, ComplaintChoice, FirstDate, LastDate)      
    except IOError:
        print "\n whoops...I/O error in creating the heatmap chart... check to make sure that the file and directory exist for the image files being created."
        
    ''' Create the scatter charts. This module saves the chart as a png file. '''
    
    try:
        CreateScatterPlot(MapData, NYCPoints, BasemapTemplate, Coordinates, ComplaintChoice, FirstDate, LastDate)     
    except IOError:
        print "\n whoops...I/O error in creating the scatter chart... check to make sure that the file and directory exist for the image files being created."
 

    CreateBoroughPiePlot(ComplaintData, FirstDate, LastDate, ComplaintChoice)