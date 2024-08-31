def is_leap_year(year : int):
    '''
    Takes an input year in int and determines whether if it is True that it is a leap year or False.
    '''
    if year % 4 != 0:    
        return(False)             #If the year isn't divisible by 4 it is not a leap year.
    else:
        if year % 100 != 0:
            return(True)          #If the year is divisible by 4 AND not divisible by 100, it IS a leap year.
        else:
            if year % 400 == 0:  
                return(True)
                
            else:
                return(False)     #If the year is divisible by 4, 100 AND NOT 400, it isn't a leap year.
                
            