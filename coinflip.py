'''
version 2.6
Minor changes to a bunch things
no change in overall opperation or function
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
        filename='log-folder\logfile{}.TXT'.format(filecounter)
        with open(filename,'x') as file:
            file.write("New run started on: {}\nStreak target: {}\nNumber of cycles: {}\n\n".format(time.asctime(),streakGoal,goal))
        break
    except FileExistsError:
        filecounter+=1
    except FileNotFoundError:
        os.mkdir('log-folder')
        print("Made new log folder") 

print("beginning run")
absolutetime=time.time()
counter=0

while goal>counter:
    counter+=1
    print("Beginning cycle {}".format(counter))
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
        file.write("cycle: {}\nflips: {}\nheads: {}\ntails: {}\ntime: {} millisecond(s)\n\n".format(counter,totalflips,streakHeadsRecord,streakTailsRecord,finalTime))

with open(filename, 'a') as file:
    file.write("Total run time: {} millisecond(s)\n".format((time.time()-absolutetime)*1000))
print("\nResults are in logfile{}".format(filecounter))
