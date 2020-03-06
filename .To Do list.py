from time import sleep
import linecache

#intros for tranfer
doingprint = "You are DOING these tasks:\n"
todoprint = "You are TO DO these tasks:\n"
doneprint = "You have DONE thse tasks:\n"
#intros for adding
doingadd = "You are adding to the DOING list"
todoadd = "You are adding to the TO DO list"
doneprint = "You are adding to the DONE list"
#intros for editing
doingedit = "You are editing the DOING list"
todoedit = "You are editing the TO DO list"
doneedit = "You are editing the DONE list"
def edit(filepath1, msg):
    print("Syntax Filler")
def transfer(filepath1, filepath2 ,msg1 ,msg2):
    #Display DOING
    with open(filepath1) as fp:
       line = fp.readline()
       cnt = 1
       print(msg1)
       while line:
           print("Task {}: {}".format(cnt, line.strip()))
           line = fp.readline()
           cnt += 1
    print(61 * '-')
    sleep(0.25)
    #Display TO DO
    with open(filepath2) as fp:

        line = fp.readline()
        cnt = 1
        print(msg2)
        while line:
            print("Task {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
    print(61 * '-')
    #User chooses task to move
    tnumchoice  = int(input("Choose a task number from the top set of tasks [x] : "))
    #file reads and assigns the line contents
    chosentask = linecache.getline(filepath1 , tnumchoice)
    #Display choice and remove unnecercary charcters
    chosentask = str(chosentask)
    chosentask = chosentask.strip("['")
    chosentask = chosentask.strip("']")
    chosentask = chosentask.strip("n")
    chosentask = chosentask.rstrip("\n")

    doing.close()
    Todo.close()

    #Adds chosen line ot another file (no base)
    with open(filepath2, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                    file_object.write("\n")
            file_object.write(chosentask)
    Todo.close
    print(61 * "-")
    print("Your task has been transferred")
    print(61 * "-")
    sleep(0.75)
    print("Removing redundant task...")
    print(61 * '-')
    sleep(0.75)

    #Removes moved task from old file (base 0)
    with open(filepath1) as f:
            tasklist = f.read().splitlines()
    tnumchoice = tnumchoice-1
    tasklist.pop(tnumchoice)
    f.close()
    with open(filepath1, 'w') as filehandle:
        filehandle.writelines("%s\n" % line for line in tasklist)
    filehandle.close()

def add_task(inputfile, msg):
        print(msg)
        print(61 * '-')
        sleep(0.25)
        taskinput = input("What task would you like to add? :")
        print("Adding task...")
        print(61 * '-')
        sleep(0.25)
        with open(inputfile, "a+") as file:
                file.seek(0)
                data = file.read(100)
                if len(data) > 0:
                        file.write("\n")
                file.write(taskinput)
        sleep(0.25)
        print("Task has been added to the list")
        print(61 * '-')
        sleep(0.25)
        print("You are being returned to the Main Menu")
        sleep(1.25)

#open all core files
doing = open("Doing.txt", "r")
Todo = open("To Do.txt" ,"r")
Done = open("Done.txt", "r")
loop = True
while loop:
        #Show menu
        print (61 * '-')
        print (20 * '-'," M A I N - M E N U " , 20 * '-')
        print (61 * '-')
        print ("1. View List")
        print ("2. Move Item")
        print ("3. Add Item")
        print ("4. Quit")
        print (61 * '-')

        #Get input
        choice = input('Enter your choice [1-4] : ')

        #Convert string to int type
        choice = int(choice)

        #Take action as per selected menu-option
        if choice == 1:

                print ("Loading Files...")
                print (61 * '-')
                print(16 * '-', " V I E W - A L L - L I S T S ", 14 * '-')
                print (61 * '-')
                print("These are the tasks you are doing:")
                print(doing.read())
                print(61 * '-')
                sleep(1.5)
                print("These are the tasks to do:")
                print(Todo.read())
                print(61 * '-')
                sleep(1.5)
                print("These are the tasks you have done:")
                print(Done.read())
                print(61 * '-')
                print("You are being returned to the Main Menu")

                sleep(1.25)

        #option for transfer code
        elif choice == 2:
                print(61 * '-')
                print ("Loading Files...")
               #Show menu
                print (61 * '-')
                print (15 * '-', " F R O M - W H I C H - L I S T? ", 12 * '-')
                print (61 * '-')
                print ("1. Doing")
                print ("2. To Do")
                print ("3. Done")
                print (61 * '-')
               #Get input
                fchoice = input('Enter your choice [1-3] : ')
                sleep(0.25)
               #Convert string to int type
                fchoice = int(fchoice)
                #Show menu
                print (61 * '-')
                print (17 * '-', " T O - W H I C H - L I S T?", 15 * '-')
                print (61 * '-')
                print ("1. Doing")
                print ("2. To Do")
                print ("3. Done")
                print (61 * '-')
               #Get input
                tchoice = input('Enter your choice [1-3] : ')
                sleep(0.25)
               #Convert string to int type
                tchoice = int(tchoice)
                #prevents copying to the same file
                if tchoice == fchoice:
                    print(61 * '-')
                    print("INVALID OPERATION")
                else:
                    #all combination of task transfer
                    if fchoice == 1 and tchoice == 2 :
                        print(61 * '-')
                        print("You have chosen to move an item from DOING to TO DO")
                        print(61 * '-')
                        transfer("Doing.txt","to do.txt" ,doingprint, todoprint)
                        print("You are being returned to the Main Menu")

                        sleep(0.25)

                    elif tchoice == 1 and fchoice == 3:
                        print(61 * '-')
                        print("You have chosen to move an item from DOING to DONE")
                        print(61 * '-')
                        transfer("Doing.txt", "done.txt" ,doingprint, doneprint)
                        print("You are being returned to the Main Menu")

                        sleep(0.25)

                    elif tchoice == 2 and fchoice == 1:
                        print(61 * '-')
                        print("You have chosen to move an item from TO DO to DOING")
                        print(61 * '-')
                        transfer("to do.txt", "doing.txt" ,todoprint, doingprint)
                        print("You are being returned to the Main Menu")

                        sleep(0.25)

                    elif tchoice == 2 and fchoice == 3:
                        print(61 * '-')
                        print("You have chosen to move an item from TO DO to DONE")
                        print(61 * '-')
                        transfer("to do.txt", "done.txt" ,todoprint, doneprint)
                        print("You are being returned to the Main Menu")

                        sleep(0.25)

                    elif tchoice == 3 and fchoice == 1:
                        print(61 * '-')
                        print("You have chosen to move an item from DONE to TO DO")
                        print(61 * '-')
                        transfer("done.txt", "to do.txt" ,doneprint, todoprint)
                        print("You are being returned to the Main Menu")

                        sleep(0.25)

                    elif tchoice == 3 and fchoice == 2:
                        print(61 * '-')
                        print("You have chosen to move an item from DOING to TO DO")
                        print(61 * '-')
                        transfer("done.txt", "to do.txt" ,doneprint, todoprint)
                        print("You are being returned to the Main Menu")

                        sleep(0.25)

        #optionn for adding a task
        elif choice == 3:
                print ("Loading Files...")
               #Show menu
                print (61 * '-')
                print (14 * '-', " ADD - T O - W H I C H - L I S T? ", 11 * '-')
                print (61 * '-')
                print ("1. Doing")
                print ("2. To Do")
                print ("3. Done")
                print (61 * '-')
               #Get input
                achoice = input('Enter your choice [1-3] : ')
                sleep(0.25)

               #Convert string to int type
                achoice = int(achoice)

                #prevents copying to the same file
                if achoice > 3:
                        print("INVALID NUMBER, HIGHER THEN 3")
                else:
                    if achoice == 1:
                            add_task("Doing.txt", doingadd)

                    if achoice == 2:
                            add_task("to do.txt", todoadd)
                    if achoice == 3:
                            add_task("done.txt", doneadd)
        elif choice == 4:
                print(25 *'-', " Q U I T ", 25 * '-')
                print("Thank you for using the to do list")
                print(61 * '-')
                loop = False

        else:
                print ("Invalid number. HIGHER THEN 4")
