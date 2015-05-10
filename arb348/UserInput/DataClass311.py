'''
A module that pulls in the initial 311 data (in a class). 

Created on May 1, 2015
@author: Adam Biesenbach
'''

import pandas as pd
import sys 

class Main311Class(object):
    '''A class to pull together the restaurant data with a number of helpful methods.'''

    def __init__(self):
        pass

    def Subset311Data(self):
        
        ''' Imports the 311 data, converts lat and long to floats, and prints a list of the unique complaint types for the
            user to choose from. '''
        try:
            self.RawDF = pd.read_csv('Data/311_Service_Requests.csv', header=0, usecols=["Created Date", "Complaint Type", "Agency", "Agency Name", "Borough", "Longitude", "Latitude", "Incident Zip"], error_bad_lines=False,  index_col=False, dtype='unicode')    
        except IOError:       
            print "\n"
            print "Sorry, there was a problem reading in the 311 data. Please check to ensure that"
            print "the file is called '311_Service_Requests.csv' and that it is in the directory at /arb348/Data."   
            sys.exit(0)
        except ValueError:
            print "\n"
            print "Sorry, there was a problem reading in the 311 data. A ValueError was thrown."
            print "the file is called '311_Service_Requests.csv' and that it is in the directory at /arb348/Data,"
            print "and make sure that it has all the columns listed in the red_csv statement."   
            sys.exit(0)
            
        # Drop rows that have a missing values.
        self.RawDF = self.RawDF[pd.notnull(self.RawDF['Created Date'])]
        self.RawDF = self.RawDF[pd.notnull(self.RawDF['Complaint Type'])]
        self.RawDF = self.RawDF[pd.notnull(self.RawDF['Latitude'])]
        self.RawDF = self.RawDF[pd.notnull(self.RawDF['Longitude'])]
        self.RawDF = self.RawDF[pd.notnull(self.RawDF['Borough'])]

        # Makes the Lat/long into floats. 
        self.RawDF[['Longitude', 'Latitude']] = self.RawDF[['Longitude', 'Latitude']].astype(float)
      
        # Create a substring that's just the date portion of the datetime variable. 
        self.RawDF['Date'] = self.RawDF['Created Date'].str[0:10]      
        
        # Replace the 'Complaint Type' observatin substring of '/' with '_', so we 
        # don't have errors when we try to name the files usning the complaint type name. 
        
        self.RawDF['Complaint Type']  = self.RawDF['Complaint Type'].str.replace('/', '_')
                
        # Index the data by 'Created Date'.
        self.RawDF.set_index("Created Date", drop =False,inplace=True)
        self.RawDF.index = pd.to_datetime(self.RawDF.index)
        
        return self.RawDF.sort()   
    

