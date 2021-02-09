'''
A basic coin flip simulation
Will ask you how many times you want to "flip the coin"
and return the total number of heads and tails and the longest streak of heads and tails in the python terminal
'''

from random import randint
from time import time

numRole=int(input("how many flips?\n\t"))
totalflips=0
heads=0
tails=0
streakHeads=0
streakTails=0
streakHeadsRecord=0
streakTailsRecord=0 
startTime=time()

while(numRole!=totalflips):
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
finalTime=int(time()-startTime)

print("With "+ str(numRole)+" total flips, you had "+str(heads)+" heads and "+str(tails)+" tails")
print("You'r best heads streak was "+str(streakHeadsRecord)+" long and you longest tails streak was "+str(streakTailsRecord))
if finalTime>0:
    print("This took "+str(finalTime)+" second(s)") 
