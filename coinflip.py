'''
version 6.1
changing the way results are written into the file to help prevent the any possible issues with simulataniums writes
'''
from random import randint
from random import seed
import time
import os
import multiprocessing

#temp seed
seed(1)

#function
def flipper(gl,filename1,c):
    print("Beginning cycle {}".format(c))
    rename=filename1+'\\cycle{}.TXT'.format(c)
    totalflips=0
    streakHeads=0
    streakTails=0
    streakHeadsRecord=0
    streakTailsRecord=0 
    startTime=time.time()*1000000
    while True:
        if gl <= streakHeadsRecord:
            break
        elif gl <= streakTailsRecord:
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
    with open(rename, 'x') as file:
        file.write("{},{},{},{},{}\n".format(c,totalflips,streakHeadsRecord,streakTailsRecord,finalTime))

if __name__ == "__main__": 
    #user inputs
    streakGoal=int(input("How long do you want the streak to be?\n\t"))
    goal=int(input("how many times do you want to run the simulation?\n\t")) 

    #creats log file and creates directory if neceissary
    filename1='tempfile'
    os.mkdir(filename1)

    print("beginning run")

    corenum=multiprocessing.cpu_count()-1
    print('{} available CPU threads.'.format(corenum))

    absolutetime=time.time()
    
    # creating a pool object 
    p = multiprocessing.Pool(processes=corenum)
    # map list to target function
    goalls=[]
    for i in range(goal):
        goalls.append((streakGoal, filename1,i+1))
    result = p.starmap(flipper, goalls)
    
    #pulls results into a single csv file
    filecounter=0
    filename=''
    while True:
        try:
            filename='results-log\logfile{}.csv'.format(filecounter)
            with open(filename,'x') as file:
                file.write("started on {}".format(time.asctime()))
                file.write("cycle,flips,heads,tails,time in microseconds\n")
            break
        except FileExistsError:
            filecounter+=1
        except FileNotFoundError:
            os.mkdir('results-log')
            print("Made new results folder") 
    
    with open(filename, 'a') as file:
        for i in range(goal):
            fileread=''
            namey=filename1+'\\cycle{}.TXT'.format(i+1)
            with open(namey, 'r') as readfile:
                fileread=readfile.readline()
            os.remove(namey)
            file.write(fileread)
            
    with open(filename, 'a') as file:            
        goal1=goal+1
        file.write("Final,=AVERAGE(B2:B{arg1}),=AVERAGE(C2:C{arg1}),=AVERAGE(D2:D{arg1}),{t}\n".format(arg1=goal1,t=(time.time()-absolutetime)*1000000))
        file.write('MAD,=AVEDEV(B2:B{g}),=AVEDEV(C2:C{g}),=AVEDEV(D2:D{g}),\n'.format(g=goal1))
        file.write('MIN,=MIN(B2:B{g}),=MIN(C2:C{g}),=MIN(D2:D{g}),\n'.format(g=goal1))
        file.write('MAX,=MAX(B2:B{})\n'.format(goal1))
    print("\nResults are in logfile{}".format(filecounter))
    os.rmdir(filename1)


