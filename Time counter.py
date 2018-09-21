##nathan broadbent
#9/21/2018
##time
import time
import calendar

def  calendar_clock():
    # Seconds
    totalSeconds= calendar.timegm(time.gmtime())
    currentSecond=totalSeconds%60
    #minutes
    totalMinutes= totalSeconds//60
    currentMinute=totalMinutes%60
    #hours
    totalHours= totalMinutes//60
    currentHour= (totalHours%24)-6

    

    print(currentHour,":",currentMinute,":",currentSecond)
   

x=0
while x==0:
    calendar_clock()
    time.sleep(1)
    
    
    
