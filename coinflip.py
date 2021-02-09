'''
version 2.5
Similar to the last version just makes the files in their own folder a directory down
Will also make the log file directory if it does not exist
'''
from random import randint
import time
import os

#user inputs
streakGoal=int(input("How long do you want the streak to be?\n\t"))
goal=int(input("how many times do you want to run the simulation?\n\t")) 

#creats log file and creates directory if neceissary
filecounter=0
filename=''
while True:
    try:
        filename='log-folder\logfile'+str(filecounter)+'.TXT'
        with open(filename,'x') as file:
            file.write("New run started on: "+str(time.asctime())+"\nStreak target: "+str(streakGoal)+"\nNumber of cycles: "+str(goal)+"\n\n")
        break
    except FileExistsError:
        filecounter+=1
    except FileNotFoundError:
        os.mkdir('log-folder')

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

