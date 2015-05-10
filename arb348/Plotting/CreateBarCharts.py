'''
Creates the bar charts of the data. 

Created on May 2, 2015
@author: Adam Biesenbach
'''

import matplotlib.pyplot as plt
import pandas as pd

def CreateAgencyBarPlots(RawDF, FirstDate, LastDate):
    '''Generates a bar plot by complaint type.'''
    try:     
        RawDF['Agency'].value_counts().head(10).plot(kind='bar',
        fontsize=10, 
        figsize=(8, 8),
        rot = 20)
        plt.xlabel("Agency Abbreviation")
        plt.ylabel("Number of Complaints")
        plt.title("311 Calls by Agency (Top 10) \n Date Range: {0} to {1}".format(FirstDate, LastDate))
        title = "Output/AgencyBarplot_" + str(pd.to_datetime(FirstDate).date()) + "_" + str(pd.to_datetime(LastDate).date()) + ".pdf"
        plt.savefig(title) 
        plt.close()
        
    except IOError:
        print "\n whoops...I/O error in creating the bar chart... check to make sure that the file and directory exist for the image files being created."
    except TypeError: 
        print "\n whoops...TypeError in creating the pie chart..."
            
def CreateBoroughBarPlots(RawDF, FirstDate, LastDate):
    '''Generates a bar plot by complaint type.'''
    try:     
        RawDF['Borough'].value_counts().plot(kind='bar',
        fontsize=10, 
        figsize=(8, 8),
        rot = 20)
        plt.xlabel("Borough")
        plt.ylabel("Number of Complaints")
        plt.title("311 Calls by Borough \n Date Range: {0} to {1}".format(FirstDate, LastDate))
        title = "Output/BoroughBarplot_" + str(pd.to_datetime(FirstDate).date()) + "_" + str(pd.to_datetime(LastDate).date()) + ".pdf"
        plt.savefig(title) 
        plt.close()
        
    except IOError:
        print "\n whoops...I/O error in creating the Borough bar chart... check to make sure that the file and directory exist for the image files being created."
    except TypeError: 
        print "\n whoops...TypeError in creating the pie chart..."
          
def CreateZIPBarPlots(RawDF, FirstDate, LastDate):
    '''Generates a bar plots of complaints by ZIP code.'''
    try:     
        RawDF['Incident Zip'].value_counts().head(10).plot(kind='bar',
        fontsize=10, 
        figsize=(8, 8),
        rot = 20)
        plt.xlabel("ZIP Code")
        plt.ylabel("Number of Complaints")
        plt.title("311 Calls by ZIP Code (Top10) \n Date Range: {0} to {1}".format(FirstDate, LastDate))
        title = "Output/ZIPBarplot_" + str(pd.to_datetime(FirstDate).date()) + "_" + str(pd.to_datetime(LastDate).date()) + ".pdf"
        plt.savefig(title) 
        plt.close()
        
    except IOError:
        print "\n whoops...I/O error in creating the ZIP code bar chart... check to make sure that the file and directory exist for the image files being created."
    except TypeError: 
        print "\n whoops...TypeError in creating the pie chart..."              