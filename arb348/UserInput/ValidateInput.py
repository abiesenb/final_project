'''
A module that runs all the user input validation functions.  

Created on Apr 10, 2015
@author: Adam Biesenbach
'''
from UserInput.ChooseComplaint import ValidateComplaintChoice
from UserInput.ChooseAgency import ValidateAgencyChoice
from UserInput.ChooseDateRange import ValidateDateChoice

def Return311Choice(RawDF):
    '''Prompt the user for input for the complaint type and date range, and return the truncated dataframe.'''
    
    (AgencyReducedDF, Agency) = ValidateAgencyChoice(RawDF)
    if Agency == 'finish':
        return ('finish','finish',RawDF,'finish','finish')
    else: 
        while True:
            (ComplaintReducedDF, Complaint) = ValidateComplaintChoice(AgencyReducedDF)
            if Complaint == 'finish':
                return ('finish','finish',RawDF,'finish','finish')    
                break
            elif Complaint == 'back':
                return ('back','back',RawDF,'back','back')        
                break
            else:
                (FirstDate, LastDate, DateReducedDF) = ValidateDateChoice(ComplaintReducedDF.sort(), Complaint)
                if FirstDate=='finish':
                    return ('finish','finish',RawDF,'finish','finish')
                    break
                elif FirstDate=='back' or LastDate=='back':
                    print 'here'
                    continue
                else:
                    return (FirstDate, LastDate, DateReducedDF, Complaint, Agency)
                    break