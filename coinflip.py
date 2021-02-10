'''
trying to inigrate basic multiprocessing to accelerate code execution 
'''
from random import randint
import time
import os

import multiprocessing 

#user inputs
streakGoal=int(input("How long do you want the streak to be?\n\t"))
goal=int(input("how many times do you want to run the simulation?\n\t")) 

#creats log file and creates directory if neceissary
filecounter=0
filename=''
while True:
    try:
        filename='log-folder\logfile{}.csv'.format(filecounter)
        with open(filename,'x') as file:
            file.write("New run started on: {}".format(time.asctime()))
            file.write("cycle,flips,heads,tails,time in microseconds\n")
        break
    except FileExistsError:
        filecounter+=1
    except FileNotFoundError:
        os.mkdir('log-folder')
        print("Made new log folder") 

print("beginning run")
counter=0

#function
def flipper():
    totalflips=0
    streakHeads=0
    streakTails=0
    streakHeadsRecord=0
    streakTailsRecord=0 
    startTime=time.time()*1000000
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
    finalTime=(time.time()*1000000)-startTime
    with open(filename, 'a') as file:
        file.write("{},{},{},{},{}\n".format(counter,totalflips,streakHeadsRecord,streakTailsRecord,finalTime))

absolutetime=time.time()
while goal>counter:
    counter+=2
    print("Beginning cycle {}".format(counter))
    if __name__ == "__main__": 
        # creating processes 
        p1 = multiprocessing.Process(target=flipper)
        p2 = multiprocessing.Process(target=flipper)
        # starting process 1 
        p1.start() 
        # starting process 2 
        p2.start() 
      
        # wait until process 1 is finished 
        p1.join() 
        # wait until process 2 is finished 
        p2.join() 
        
with open(filename, 'a') as file:
    goal1=goal+1
    file.write("Final,=AVERAGE(B2:B{}),=AVERAGE(C2:C{}),=AVERAGE(D2:D{}),{}\n".format(goal1,goal1,goal1,(time.time()-absolutetime)*1000000))
    file.write('MAD,=AVEDEV(B2:B{}),=AVEDEV(C2:C{}),=AVEDEV(D2:D{}),\n'.format(goal1,goal1,goal1))
    file.write('MIN,=MIN(B2:B{}),=MIN(C2:C{}),=MIN(D2:D{}),\n'.format(goal1,goal1,goal1))
    file.write('MAX,=MAX(B2:B{})\n'.format(goal1))
print("\nResults are in logfile{}".format(filecounter))
