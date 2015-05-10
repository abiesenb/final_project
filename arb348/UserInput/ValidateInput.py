'''
A module that runs all the user input validation functions.  

Created on Apr 10, 2015
@author: Adam Biesenbach
'''
from UserInput.ChooseComplaint import ValidateComplaintChoice
from UserInput.ChooseAgency import ValidateAgencyChoice
from UserInput.ChooseDateRange import ValidateDateChoice

def Return311Choice(RawDF):
    '''Prompt the user for input for the complaint type and date range, and return the truncated dataframe.
    Note that if they return "finish" or "break", we still need to return a 5-d tuple, so we fill the missing
    entries with the user's input. 
    '''
    
    (AgencyReducedDF, Agency) = ValidateAgencyChoice(RawDF)
    # If they want to exit, break the loop.
    if Agency == 'finish':
        return ('finish','finish',RawDF,'finish','finish')
    else: 
        while True:
            (ComplaintReducedDF, Complaint) = ValidateComplaintChoice(AgencyReducedDF)
            # If they want to exit, break the loop.
            if Complaint == 'finish':
                return ('finish','finish',RawDF,'finish','finish')    
                break
            # If they want to go back, break the loop.
            elif Complaint == 'back':
                return ('back','back',RawDF,'back','back')        
                break
            else:
                
                (FirstDate, LastDate, DateReducedDF) = ValidateDateChoice(ComplaintReducedDF.sort(), Complaint)
                # If they want to exit, break the loop.
                if FirstDate=='finish':
                    return ('finish','finish',RawDF,'finish','finish')
                    break
                # If they want to go back, break the loop.
                elif FirstDate=='back' or LastDate=='back':
                    print 'here'
                    continue
                else:
                    return (FirstDate, LastDate, DateReducedDF, Complaint, Agency)
                    break