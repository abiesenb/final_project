'''
This is the main project module for the final project. 

Created on Apr 10, 2015
@author: Adam Biesenbach
'''

import sys
from UserInput.DataClass311 import Main311Class
from Plotting.CreatePlots import CreatePlots

if __name__  =='__main__':h
    
    try:
        
        '''The Import311Data class itself generates a object containing the 
        complaint data as a pandas data frame. Here we call the  Subset311Data method,  
        which imports and cleans the data (removes observations with missing values, etc.). '''
        
        print "\n"        
        print "Loading 311 file... this will take a few moments..."
        print "\n"
                    
        RawDF = Main311Class().Subset311Data()
        
        '''The CreatePlots function prompts the user for input (complaint type, date range), 
        and create the choropleth, scatter and other charts.'''
       
        CreatePlots(RawDF)
       
        '''If the user types 'finish', exit.'''
        
        print "\n"
        print "Exiting program."
        print "\n"
        
        sys.exit(0)
                
    except KeyboardInterrupt:
        print "\n whoops... KeyboardInterrupt... exiting program."
        sys.exit(0)    
        