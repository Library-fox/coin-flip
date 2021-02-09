'''
Code now writes results directly to a text file
Uses the custom module "timefix" to create the files name
'''
from random import randint
import time

#user inputs
streakGoal=int(input("How long do you want the streak to be?\n\t"))
goal=int(input("how many times do you want to run the simulation?\n\t")) 

#creates logfile
import timefix
filename='log '+str(timefix.finalstring)+'.TXT'
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

