'''
A module defining project-specific exceptions.

Created on May 10, 2015
@author: Adam Biesenbach
'''

import sys 


class MissingFile(Exception):
    '''
    Exception raised if the 311 file is missing.
    '''
    def __str__(self):
        print "\n"
        print "Sorry, there was a problem reading in the 311 data. Please check to ensure that"
        print "the file is called '311_Service_Requests.csv' and that it is in the directory at /arb348/Data."   
        sys.exit(0)
        
class Missing311Data(Exception):
    '''
    Exception raised if the 31i read_csv import throws a ValueError-- likely because of missing columns.
    '''
    def __str__(self):
            print "\n"
            print "Sorry, there was a problem reading in the 311 data. A ValueError was thrown."
            print "the file is called '311_Service_Requests.csv' and that it is in the directory at /arb348/Data,"
            print "and make sure that it has all the columns listed in the red_csv statement."    
            
class AgencyBarIO(Exception):
    '''
    Exception raised if the Agency bar chart file has an IO issue.
    '''
    def __str__(self):
        print "\n whoops...I/O error in creating the agency bar chart... check to make sure that the file and directory exist for the image files being created."

class BoroughBarIO(Exception):
    '''
    Exception raised if the Borough bar chart file has an IO issue.
    '''
    def __str__(self):
        print "\n whoops...I/O error in creating the Borough bar chart... check to make sure that the file and directory exist for the image files being created."


class ZIPBarIO(Exception):
    '''
    Exception raised if the ZIP bar chart file has an IO issue.
    '''
    def __str__(self):
        print "\n whoops...I/O error in creating the ZIP code bar chart... check to make sure that the file and directory exist for the image files being created."

class HeatMapIO(Exception):
    '''
    Exception raised if the heatmap chart file has an IO issue.
    '''
    def __str__(self):
        print "\n whoops...I/O error in creating the heatmap chart... check to make sure that the file and directory exist for the image files being created."

class ScatterPlotIO(Exception):
    '''
    Exception raised if the scatterplot file has an IO issue.
    '''
    def __str__(self):
        print "\n whoops...I/O error in creating the scatter chart... check to make sure that the file and directory exist for the image files being created."

