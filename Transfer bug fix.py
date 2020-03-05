from time import sleep
import linecache

doing = open("Doing.txt", "r")
Todo = open("To Do.txt" ,"r")
Done = open("Done.txt", "r")

#intros for tranfer
doingprint = "You are DOING these tasks:\n"
todoprint = "You are TO DO these tasks:\n"
doneprint = "You have DONE thse tasks:\n"
#intros for adding
doingadd = "You are adding to the DOING list"
todoadd = "You are adding to the TO DO list"
doneprint = "You are adding to the DONE list"


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
    sleep(0.25)
    print("Removing redundant task...")
    print(61 * '-')
    
    #Removes moved task from old file (base 0)
    with open(filepath1) as f:
            tasklist = f.read().splitlines()
    tnumchoice = tnumchoice-1
    tasklist.pop(tnumchoice)
    f.close()
    with open(filepath1, 'w') as filehandle:
        filehandle.writelines("%s\n" % line for line in tasklist)
    filehandle.close()
print(61 * '-')
print("You have chosen to move an item from DOING to TO DO")
print(61 * '-')
transfer("Doing.txt","to do.txt" ,doingprint, todoprint)
print("Thank you for using TO DO list")
print(61 * '-')
