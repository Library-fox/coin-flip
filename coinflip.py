'''
Almost identical to version 2.2, just no longer requires the timefix module as its code has been directly intigrated
'''
from random import randint
import time

#user inputs
streakGoal=int(input("How long do you want the streak to be?\n\t"))
goal=int(input("how many times do you want to run the simulation?\n\t")) 

#creates logfile name

#base working string
basestring= time.asctime()

#isolates clock
stringclock=basestring
length1=len(stringclock)
length1=length1-13
stringclock=stringclock[length1:]
stringclock=stringclock[:-5]
lengthclock=len(stringclock)+1

#isolates hours minutes and seconds
stringtime=stringclock
hours=stringtime[:-6]
minutes=stringtime[3:-3]
seconds=stringtime[6:]

#converts time bits back into a single string
finalclock=str(hours)+';'+str(minutes)+';'+str(seconds)

#isolates year
stringyear=basestring
length=len(stringyear)
stringyear=stringyear[-4:]
lengthyear=len(stringyear)+1

#isolates day 
stringday=basestring
cutlength1=lengthyear+lengthclock
stringday=stringday[4:]
stringday=stringday[:-cutlength1]
stringmonth=stringday #for later
stringday=stringday[5:]

#isolates month
length2=len(stringmonth)
length2=length2-3
stringmonth=stringmonth[:length2]

#strings everything back together into a date and time
finalstring=stringmonth+' '+stringday+' '+stringyear+' '+finalclock

#creates logfile
filename='log '+str(finalstring)+'.TXT'
with open( str(filename), 'a') as file:
    file.write("New simulation started on: "+str(time.asctime())+"\nStreak target: "+str(streakGoal)+"\number of cycles: "+str(goal)+"\n\n")


print("beginning run")
absolutetime=time.time()
counter=0

while goal>counter:
    counter+=1
    print("Beginning cycle "+str(counter))
    totalflips=0
    streakHeads=0
    streakTails=0
    streakHeadsRecord=0
    streakTailsRecord=0 
    startTime=time.time()*1000

    while True:
        if streakGoal <= streakHeadsRecord:
            break
        elif streakGoal <= streakTailsRecord:
            break
        totalflips+=1
        flip=randint(0,1)
        if flip == 0:
            streakHeads+=1
            streakTails=0
            if streakHeads > streakHeadsRecord:
                streakHeadsRecord=streakHeads
        elif flip == 1:
            streakTails+=1
            streakHeads=0
            if streakTails > streakTailsRecord:
                streakTailsRecord=streakTails
    finalTime=(time.time()*1000)-startTime
    with open(filename, 'a') as file:
        file.write("cycle: "+str(counter)+'\n')
        file.write("flips: "+str(totalflips)+'\n')
        file.write("heads: "+str(streakHeadsRecord)+"\ntails: "+str(streakTailsRecord)+'\n')
        file.write("time: "+str(finalTime)+" millisecond(s)\n\n")
with open(filename, 'a') as file:
    file.write("Total run time: "+str((time.time()-absolutetime)*1000)+' millisecond(s)\n')

