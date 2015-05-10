'''
Creates the bar charts of the data. 

Created on May 2, 2015
@author: Adam Biesenbach
'''

import matplotlib.pyplot as plt
import pandas as pd
import Exceptions

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
        raise Exceptions.AgencyBarIO()
       
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
        raise Exceptions.BoroughBarIO()

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
        raise Exceptions.ZIPBarIO()   