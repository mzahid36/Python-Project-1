#importing libraries 
import datetime
from playsound import playsound

def initial_decoration():
    # This section of code only for decoration purpose.
    print()
    print('-'*40)
    print('-','\tProject 1 : Alarm Clock',' '*6,'-')
    print('-'*40,'\n\n')
    #decoration ends here

# This function contains all about user input and error handling
def user_input():    
    try:
        #user input section (Hour - Minutes - am/pm)
        print('--Time format 12h.--\n')
        global hour
        hour = int(input('Enter Hour : '))
        global minutes
        minutes = int(input('Enter Minutes : '))
        am_pm = input('am / pm : ')

        if (hour > 12 or hour < 0) or (minutes > 60 or minutes < 0) or (am_pm != 'am' and am_pm != 'pm'):
            # print('Please enter correct time.') 
            raise Exception
        if am_pm == 'pm':
            hour += 12

    except Exception:
        print('\nFound Error: Please enter correct time.\n')

    else:
        if am_pm == 'am':
            print('\nYour alarm time is - ',hour,':',minutes,':',am_pm)
        else:
            print('\nYour alarm time is - ',hour-12,':',minutes,':',am_pm)

# this function deals with the alarm and alarm sound
def alarm(hour,minutes):
    while True:
        if hour == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute:
            print('Playing')
            playsound('Morning Alarm -.mp3')
            break

initial_decoration()
user_input()
alarm(hour,minutes)


