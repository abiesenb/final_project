'''
A Test module for the final project. 

Created on May 2, 2015
@author: Adam Biesenbach
'''

import unittest
import os.path
import pandas as pd 

class Test(unittest.TestCase):
    
    def test311(self):
        '''Tests if the 311 data file exits in the Data directory.'''

        self.assertTrue(os.path.exists("./Data/311_Service_Requests.csv"), "The 311 data set needs to be in the /Data directory and that it's called 311_Service_Requests.csv.")
        self.assertTrue(os.path.exists("./Data/nycd_corrected.dbf"), "The shapefile nycd_corrected.dbf isn't in the data directory.")
        self.assertTrue(os.path.exists("./Data/nycd_corrected.prj"), "The shapefile nycd_corrected.dbf isn't in the data directory.")
        self.assertTrue(os.path.exists("./Data/nycd_corrected.qpj"), "The shapefile nycd_corrected.dbf isn't in the data directory.")
        self.assertTrue(os.path.exists("./Data/nycd_corrected.shp"), "The shapefile nycd_corrected.dbf isn't in the data directory.")
        self.assertTrue(os.path.exists("./Data/nycd_corrected.shx"), "The shapefile nycd_corrected.dbf isn't in the data directory.")

    def testColumnsInDF(self):
        '''Tests if the 311 data has the necessary columns.'''
        
        self.RawDF = pd.read_csv('Data/311_Service_Requests.csv', header=0, usecols=["Created Date", "Complaint Type", "Agency", "Agency Name", "Borough", "Longitude", "Latitude", "Incident Zip"], error_bad_lines=False,  index_col=False, dtype='unicode')    
        self.assertTrue( 'Created Date' in self.RawDF,  "311 data missing created date column.")
        self.assertTrue( 'Complaint Type' in self.RawDF,  "311 data missing 'Complaint Type' column.")
        self.assertTrue( 'Agency' in self.RawDF,  "311 data missing 'Agency' column.")
        self.assertTrue( 'Borough' in self.RawDF,  "311 data missing 'Borough' column.")
        self.assertTrue( 'Latitude' in self.RawDF,  "311 data missing 'Latitude' column.")
        self.assertTrue( 'Longitude' in self.RawDF,  "311 data missing 'Longitude' column.")
        self.assertTrue( 'Incident Zip' in self.RawDF,  "311 data missing 'Incident Zip' column.")

        
if __name__ == "__main__":
  
    unittest.main()