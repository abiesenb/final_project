'''
Creates the pie charts of the data. 

Created on May 2, 2015
@author: Adam Biesenbach
'''

import matplotlib.pyplot as plt
import pandas as pd

def CreateAllComplaintPiePlot(RawDF, FirstDate, LastDate):
    '''Generates a pie plots by complaint type.'''
    
    try:
        RawDF['Complaint Type'].value_counts().head(10).plot(kind='pie',
        fontsize=10,
        figsize=(10, 10))
        plt.title("311 Calls by Complaint Type (Top 10) \n Date Range: {0} to {1}".format(FirstDate, LastDate))
        title = "Output/ComplaintPieplot_" + str(pd.to_datetime(FirstDate).date()) + "_" + str(pd.to_datetime(LastDate).date()) + ".pdf"
        plt.savefig(title) 
        plt.close()
    except IOError:
        print "\n whoops...I/O error in creating the pie chart... check to make sure that the file and directory exist for the image files being created."
    except TypeError: 
        print "\n whoops...TypeError in creating the pie chart..."
        
def CreateBoroughPiePlot(RawDF, FirstDate, LastDate, ComplaintChoice):
    '''Generates a pie plots by Borough.'''
    
    try:
        RawDF['Borough'].value_counts().head(10).plot(kind='pie',
        fontsize=10, 
        figsize=(10, 10))
        plt.title("311 {0} Calls by Borough \n Date Range: {1} to {2}".format(ComplaintChoice, FirstDate, LastDate))
        title = "Output/BoroughPieplot_" + str(pd.to_datetime(FirstDate).date()) + "_" + str(pd.to_datetime(LastDate).date()) + ".pdf"
        plt.savefig(title) 
        plt.close()
        
    except IOError:
        print "\n whoops...I/O error in creating the Borough pie chart... check to make sure that the file and directory exist for the image files being created."
    except TypeError: 
        print "\n whoops...TypeError in creating the pie chart..."
        
