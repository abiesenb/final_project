'''
A Test module for the final project. 

Created on May 2, 2015
@author: Adam Biesenbach
'''

import unittest
import os.path

class Test(unittest.TestCase):
    '''Tests if the 311 data file exits in the Data directory.'''
    
    def test311(self):
    
        self.assertTrue(os.path.exists("./Data/311_Service_Requests.csv"), "The 311 data set needs to be in the /Data directory and that it's called 311_Service_Requests.csv.")
        self.assertTrue(os.path.exists("./Data/nycd_corrected.dbf"), "The shapefile nycd_corrected.dbf isn't in the data directory.")
        self.assertTrue(os.path.exists("./Data/nycd_corrected.prj"), "The shapefile nycd_corrected.dbf isn't in the data directory.")
        self.assertTrue(os.path.exists("./Data/nycd_corrected.qpj"), "The shapefile nycd_corrected.dbf isn't in the data directory.")
        self.assertTrue(os.path.exists("./Data/nycd_corrected.shp"), "The shapefile nycd_corrected.dbf isn't in the data directory.")
        self.assertTrue(os.path.exists("./Data/nycd_corrected.shx"), "The shapefile nycd_corrected.dbf isn't in the data directory.")

if __name__ == "__main__":
  
    unittest.main()