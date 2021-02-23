'''
version 7.1
changing some stuff with the results log
formating, data included etc
nothing to to major
also changed/updated some of the comments 
'''
from random import randint
from random import seed
import time
import os
from multiprocessing import Pool, cpu_count

beginTime=time.asctime()

#function
def flipper(gl,filename1,c):
    print("Beginning cycle {}".format(c))
    rename=filename1+'\\cycle{}.TXT'.format(c)
    totalflips=0
    streakHeads=0
    streakTails=0
    heads=0
    tails=0
    streakHeadsRecord=0
    streakTailsRecord=0 
    startTime=time.time()
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
            heads+=1
            if streakHeads > streakHeadsRecord:
                streakHeadsRecord=streakHeads
        elif flip == 1:
            streakTails+=1
            streakHeads=0
            tails+=1
            if streakTails > streakTailsRecord:
                streakTailsRecord=streakTails
    finalTime=time.time()-startTime
    with open(rename, 'x') as file:
        file.write("{},{},{},{},{}\n".format(c,totalflips,heads,tails,finalTime))

if __name__ == "__main__": 
    #user inputs
    streakGoal=int(input("How long do you want the streak to be?\n\t"))
    goal=int(input("how many times do you want to run the simulation?\n\t")) 

    #creats temporary write file
    filename1='tempfile'
    os.mkdir(filename1)

    print("beginning run")

    corenum=cpu_count()-1
    print('{} available CPU threads.'.format(corenum))

    absolutetime=time.time()
    
    #creates and initiates pool
    p = Pool(processes=corenum)
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
                file.write("started on {}\n".format(beginTime))
                file.write("cycle,total flips,heads,tails,cycle time (secs)\n")
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
    
    #appends excel functions to the bottom of the file
    with open(filename, 'a') as file:            
        goal1=goal+2
        file.write("Total,=SUM(B3:B{arg1}),=SUM(C3:C{arg1}),=SUM(D3:D{arg1}),{t}\n".format(arg1=goal1,t=(time.time()-absolutetime)))
        file.write("Average,=AVERAGE(B3:B{arg1}),=AVERAGE(C3:C{arg1}),=AVERAGE(D3:D{arg1})\n".format(arg1=goal1))
        file.write('MAD,=AVEDEV(B3:B{g}),=AVEDEV(C3:C{g}),=AVEDEV(D3:D{g}),\n'.format(g=goal1))
        file.write('MIN,=MIN(B3:B{g}),=MIN(C3:C{g}),=MIN(D3:D{g}),\n'.format(g=goal1))
        file.write('MAX,=MAX(B3:B{g}),=MAX(C3:C{g}),=MAX(D3:D{g})\n'.format(g=goal1))
    print("\nResults are in logfile{}".format(filecounter))
    
    #deletes temporary write file
    os.rmdir(filename1)
