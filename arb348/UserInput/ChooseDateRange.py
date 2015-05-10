'''
This module contains the function for validating the user's date input. 

Created on Apr 12, 2015
@author: Adam Biesenbach
'''

import pandas as pd
import sys

def ValidateDateChoice(RawDF, Complaint):
    ''' Validate the date choices the user makes. Returns a reduced data containing only those observations
    between those two dates.'''
  
    while True:
        try:
            print '\n'
            print (60 * '-')
            print ("Which dates are you interested in?")
            print '\n'
            print ("The date range of observations for the complaint")
                    
            minDate = str(pd.to_datetime(RawDF["Created Date"]).min().date())
            maxDate = str(pd.to_datetime(RawDF["Created Date"]).max ().date())
            
            print ("you selected is: " + minDate + " through " + maxDate)
            print '\n'
            print ("To select the maximum date range, type 'max'.")
            print '\n'
            print ("To return to the complaint menu, type 'back'.")
            print '\n'      
            print ("If you'd like to exit, type 'finish'.")        
            print (60 * '-')   
            print "\n"
            
            # Get their first date entry.
            FirstDate = raw_input('Start date (yyyy-mm-dd format please)? ' )
            
            # Check to make sure the date is in the range provided for that 
            # complaint choice. If 'wrong', prompt again. If 'right', move on to
            # the end date choice and perform the analogous analysis. If they enter
            # 'back', break the loop so we can return to the previous menu. If 
            # they enter 'max' at either prompt, use the maximum date range available.
            # If they enter valid input at both prompts, return the truncated 
            # data.
            
            FirstChecker = CheckDate(RawDF, FirstDate)
            if FirstChecker == 'right':
                print "\n"
                LastDate = raw_input('Ending date (yyyy-mm-dd  format please)? ' )
                SecondChecker = CheckDate(RawDF, LastDate)
                if SecondChecker == 'right':
                    
                    # Ending date must not precede beginning date. 
                    if pd.to_datetime(FirstDate)<=pd.to_datetime(LastDate): 
                        break
                    else:
                        print 'Invalid choices: Starting date must precede ending date.'
                        continue
                elif SecondChecker =='wrong':
                    print "\n"
                    print "Sorry, incorrect input. Please try again."
                    continue
                elif SecondChecker=='finish':
                    print 'Exiting program.' 
                    return ('finish', 'finish', RawDF)   
                    break
                elif SecondChecker=='back':
                    return ('back', 'back', RawDF)   
                    break
                elif SecondChecker=='max':
                    return (minDate, maxDate, RawDF[minDate:maxDate])
            elif FirstChecker == 'wrong':
                print "\n"
                print "Sorry, incorrect input. Please try again."
                continue
            elif FirstChecker=='finish':
                print 'Exiting program.'
                return ('finish', 'finish', RawDF)
                break
            elif FirstChecker=='back':
                print 'Exiting program.'
                return ('back', 'back', RawDF)
                break           
            elif FirstChecker=='max':
                return (minDate, maxDate, RawDF[minDate:maxDate])
        except KeyboardInterrupt:
            print "\n whoops... KeyboardInterrupt... exiting program."
            sys.exit(0)
    
    return (FirstDate, LastDate, RawDF[FirstDate:LastDate])

def CheckDate(RawDF, date):
    ''' Check that the date the user provided is in the date range for the complaint 
    type selected. '''
    
    if date !="" :
            if date=='finish' :
                return 'finish'
            elif date=='back':
                return 'back'
            elif date=='max':
                return 'max'
            else:
                First = pd.to_datetime(RawDF["Created Date"]).min().date()
                Last  = pd.to_datetime(RawDF["Created Date"]).max().date()
                try:
                    if (( pd.to_datetime(date).date() >= First ) and ( pd.to_datetime(date).date() <= Last )):
                        return 'right'
                    else:
                        return 'wrong'
                except AttributeError:
                        return 'wrong'
    else:
        return 'wrong'


