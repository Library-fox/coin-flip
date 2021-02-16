'''
version 4.1
trying to inigrate basic multiprocessing to accelerate code execution
'''
'''
well, that went terribly
but it works, sure its slower than it was before but hey it works!
onto the next version where ill scrap all that i just did and start over with the multi procressing.
'''
from random import randint
import time
import os
import multiprocessing
import workingfunction

if __name__ == "__main__": 
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
                file.write("thread,flips,heads,tails,time in microseconds\n")
            break
        except FileExistsError:
            filecounter+=1
        except FileNotFoundError:
            os.mkdir('log-folder')
            print("Made new log folder") z

    print("beginning run")
    counter=0


    #marks simulation start time
    absolutetime=time.time()


    while goal>counter:

        
        #creating process 1
        counter+=1
        p1 = multiprocessing.Process(target=workingfunction.flipper,args=(streakGoal,filename,counter))
        p1.start()
        print("Beginning cycle {}".format(counter))
        
        #creating process 2
        counter+=1
        p2 = multiprocessing.Process(target=workingfunction.flipper,args=(streakGoal,filename,counter))
        p2.start()
        print("Beginning cycle {}".format(counter))

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
     
