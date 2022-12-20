# This section of code only for decoration purpose.
print()
print('-'*40)
print('-','\tProject 1 : Alarm Clock',' '*6,'-')
print('-'*40,'\n\n')
#decoration ends here

#user input section (Hour - Minutes - am/pm)
hour = int(input('Enter Hour : '))
minutes = int(input('Enter Minutes : '))
am_pm = input('am / pm : ')

if (hour > 12 or hour < 0) or (minutes > 60 or minutes < 0 ) or ( am_pm != 'am' and am_pm != 'pm'):
    print('Please enter correct time.') 

