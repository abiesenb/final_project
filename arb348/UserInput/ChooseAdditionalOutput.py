'''
A function for prompting the user for whether or not they'd like additional
output for the date range they've selected. 

Created on May 5, 2015
@author: Adam Biesenbach
'''

import sys

def ValidateAddChartChoice():
    
    while True:
        try:        
            print '\n'
            print (60 * '-')
            choice = raw_input("Would you like additional analysis for this date range (yes/no)? Exit by typing 'finish'.")
            print '\n'
            print (60 * '-')

        except KeyboardInterrupt:
            print "\n whoops... KeyboardInterrupt... exiting program."
            sys.exit(0)
        
        if choice == 'yes' or choice =='no' or choice == 'finish':
            return choice 
            break
        else:
            print "sorry, response must be 'yes', 'no' or 'finish'."
            continue