'''
A module for validating the user's agency choice. 

Created on May 5, 2015
@author: Adam Biesenbach
'''

import sys
import pandas as pd 

def ValidateAgencyChoice(RawDF):
    ''' Validate the complaint choice the user makes. Returns the reduced data containing only those complaints.'''
    
    # Make a dict of Agencies to loop over.  
    Agencies = GetAgencyDict(RawDF)
    while True:
        # Get the user's agency choice.
        choice = GetAgencyChoice(RawDF)   
        # Make sure they enter something. If not, prompt again.     
        if choice !="":
            # If they want to exit, break the loop. Otherwise, see if the choice 
            # is valid. If so, return the truncated data.
            if choice=='finish':
                break
            else:
                try:
                    if int(choice) in Agencies:
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
    if choice =='finish':
        return (RawDF, 'finish')
    else: 
        return (RawDF[RawDF["Agency"] ==Agencies[int(choice)]], Agencies[int(choice)])

def GetAgencyChoice(RawDF):
    '''Return the raw input from the user containing the complaint type.'''
    
    # Produce the dictionary of agencies and identifiers for displaying.  
    Agencies = GetAgencyDict(RawDF)
    
    print '\n'
    print (60 * '-')
    print ("Which agency calls are you interested in?")
    print ("Choose a number from the 'Department ID' list below.")
    print '\n'
    print ("If you'd like to exit, type 'finish'.")        
    print (60 * '-')
    print pd.DataFrame(Agencies.items(), columns=['Department ID', 'Agency']).to_string(index=False)
    print (60 * '-') 
    
    try:      
        print "\n"
        choice =  raw_input("Please Enter Here: ")
    except KeyboardInterrupt:
        print "\n whoops... KeyboardInterrupt... exiting program."
        sys.exit(0)
    else: 
        return choice 

def GetAgencyDict(RawDF):
    """Create a dictionary of agencies which integer identifiers."""
    
    Agencies = {} 
    for i in range(len(RawDF["Agency"].unique())):
        Agencies[i] = RawDF["Agency"].unique()[i]
    return Agencies    
        
