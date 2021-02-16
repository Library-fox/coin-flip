#working function
import time
from random import randint

#function
def flipper(streakgoal,filename,counter):
    totalflips=0
    streakHeads=0
    streakTails=0
    streakHeadsRecord=0
    streakTailsRecord=0 
    startTime=time.time()*1000000
    while True:
        if streakgoal <= streakHeadsRecord:
            break
        elif streakgoal <= streakTailsRecord:
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
    finalTime=(time.time()*1000000)-startTime
    with open(filename, 'a') as file:
        file.write("{},{},{},{},{}\n".format(counter,totalflips,streakHeadsRecord,streakTailsRecord,finalTime))