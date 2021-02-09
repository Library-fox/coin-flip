'''
uses the 
'''
from random import randint
from time import time

streakGoal=int(input("How long do you want the streak to be?\n\t"))

counter=0 
while counter<10:
    counter+=1
    totalflips=0
    heads=0
    tails=0
    streakHeads=0
    streakTails=0
    streakHeadsRecord=0
    streakTailsRecord=0 
    startTime=time()*1000

    while True:
        if streakGoal <= streakHeadsRecord:
            break
        elif streakGoal <= streakTailsRecord:
            break
        totalflips+=1
        flip=randint(0,1)
        if flip == 0:
            heads+=1
            streakHeads+=1
            streakTails=0
            if streakHeads > streakHeadsRecord:
                streakHeadsRecord=streakHeads
        elif flip == 1:
            tails+=1
            streakTails+=1
            streakHeads=0
            if streakTails > streakTailsRecord:
                streakTailsRecord=streakTails
    finalTime=int((time()*1000)-startTime)
    with open('fliplog1.TXT', 'a') as file:
        file.write("It took "+str(totalflips)+" flips to reach a streak of "+str(streakGoal)+'\n')
        file.write("The best heads streak was "+str(streakHeadsRecord)+" and the best tails streak was "+str(streakTailsRecord)+'\n')
        file.write("This took "+str(finalTime)+" milliseconds(s)\n\n") 
