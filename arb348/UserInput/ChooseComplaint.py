'''
A module for validating the user's complaint choice. 

Created on May 5, 2015
@author: Adam Biesenbach
'''

import sys
import pandas as pd 

def ValidateComplaintChoice(RawDF):
    ''' Validate the complaint choice the user makes. Returns the reduced data containing only those complaints.'''
    
    # Make a dict of unique complaints.
    Complaints = GetComplaintDict(RawDF)    
    while True:
        # Get users complaint choice
        choice = GetComplaintChoice(RawDF)        
        # Make sure they entered something. If not, prompt again. If they did,
        # validate their choice. If it's invalid, prompt again. Otherwise, 
        # return the truncated data. 
        
        if choice !="":
            if choice=='finish' or choice == 'back':
                break
            else:
                try:
                    if int(choice) in Complaints:
                        break
                    else:
                        print "\n"
                        print "Invalid choice."
                        continue
                except ValueError:
                    print "\n"
                    print "Invalid choice."
                    continue
        else:
            print "\n"
            print "Invalid choice."   
            continue
    if choice =='finish' or choice=='back':
        return (RawDF, choice)
    else: 
        return (RawDF[RawDF["Complaint Type"] == Complaints[int(choice)]], Complaints[int(choice)])

def GetComplaintChoice(RawDF):
    '''Return the raw input from the user containing the complaint type.'''
    
    # Produce the dictionary of agencies and identifiers for displaying.  
    Complaints = GetComplaintDict(RawDF)
    
    print '\n'
    print (60 * '-')
    print ("Which complaints are you interested in?")
    print ("Choose a number from the 'Complaint ID' list below.")
    print '\n'
    print ("To return to the Agency menu, type 'back'.")
    print '\n'
    print ("If you'd like to exit, type 'finish'.")        
    print (60 * '-')
    print pd.DataFrame(Complaints.items(), columns=['Complaint ID', "Complaint Type"]).to_string(index=False)
    print (60 * '-') 
    
    try:      
        print "\n"
        choice =  raw_input("Please Enter Here: ")
    except KeyboardInterrupt:
        print "\n whoops... KeyboardInterrupt... exiting program."
        sys.exit(0)
    else: 
        return choice 

def GetComplaintDict(RawDF):
    """Create a dictionary of agencies which integer identifiers."""
    
    Complaints = {} 
    for i in range(len(RawDF["Complaint Type"].unique())):
        Complaints[i] = RawDF["Complaint Type"].unique()[i]
    return Complaints    
        
