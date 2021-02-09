'''
Instead of asking for a number of total flips the program will ask for a "streak goal"
since the final target for this simulation is based on luck it can take signifactly longer to complete than version 1
'''
from random import randint
from time import time

streakGoal=int(input("How long do you want the streak to be?\n\t"))
totalflips=0
heads=0
tails=0
streakHeads=0
streakTails=0
streakHeadsRecord=0
streakTailsRecord=0 
startTime=time()

while True:
    if streakGoal <= streakHeadsRecord:
        break
    elif streakGoal <= streakTailsRecord:
        break
    totalflips+=1
    print("Running cycle: "+str(totalflips))
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
finalTime=int(time()-startTime)

print("It took "+str(totalflips)+" flips to reach a streak of "+str(streakGoal))
print("The best heads streak was "+str(streakHeadsRecord)+" and the best tails streak was "+str(streakTailsRecord))
if finalTime>0:
    print("This took "+str(finalTime)+" second(s)") 
