print("You have chosen to move an item from DOING to TO DO")
print(40 * '-')
#Display DOING
filepath = 'Doing.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   print("You are doing these tasks:\n")
   while line:
       print("Task {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
print(40 * '-')      
sleep(0.25)
#Display TO DO
filepath = 'to do.txt'
with open(filepath) as fp:
    
    line = fp.readline()
    cnt = 1
    print("You are to do these tasks:\n")
    while line:
        print("Task {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1
print(40 * '-')
#User chooses task to move 
tnumchoice  = int(input("Choose a task number from DOING [x] : "))
lines = doing.readlines()
#file readsa and assigns the line contents
chosentask = linecache.getline("doing.txt" , tnumchoice)
#Display choiceand remove unnecercary charcters
chosentask = str(chosentask)
chosentask = chosentask.strip("['")
chosentask = chosentask.strip("']")
chosentask = chosentask.strip("n")
chosentask = chosentask.rstrip("\n")


doing.close()
Todo.close()
#Adds chosen line ot another file (no base)
with open("To do.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
                file_object.write("\n")
        file_object.write(chosentask)
Todo.close
print(40 * "-")
print("Your task has been transferred")
print(40 * "-")
print("Removing redundant task...")
#Removes moved task from old file (base 0)
with open("doing.txt") as f:
        tasklist = f.read().splitlines()
tnumchoice = tnumchoice-1
tasklist.pop(tnumchoice)
f.close()
with open('doing.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % line for line in tasklist)
doing.close()

