# Advent of Code 2022 :: Day 07

# Read in the data from terminal. 
terminal_file = open("day07-data.txt","r")
terminal_raw = terminal_file.read()
terminal_file.close()

# Collect lines of terminal readout into a list. 
terminal_readout = terminal_raw.split("\n")

# Need to keep track of: 
#   [ ] :: Current directory
#   [ ] :: Parent directory
#   [ ] :: Subdirectories directory
#   [ ] :: Current directory files
#   [ ] :: Current directory total size
#   [ ] :: 
#   [ ] :: 
#   [ ] :: 

# This dictionary is to store all directories.
directories = {
    "/" : {"name" : "/",
           "parent" : None,
           "files" : [],
           "subdirectories" : [],
           "size" : 0}
           }

# This dictionary keeps track of current place in file system.
current_directory = {
    "name" : "/",
    "parent" : None,
    }

# This method uses a cd command to change the current directory.
def change_directory(command):

    """
        Things that happen when cd command made:

            [ ] :: Change the current directory.
    
        command = $ cd <name>
    
    """

    # Get the name of the new directory from end of command.
    new_directory = command[5:]

    if new_directory == "..":
        # In this case we are going out one level.
        current_directory["name"] = current_directory["parent"]
        current_directory["parent"] = directories[current_directory["name"]]["parent"]
    
    elif new_directory == "/":
        # In this case we are going to Home directory.
        current_directory["name"] = "/"
        current_directory["parent"] = None
    
    else:
        # In this case we are going in one level.
        current_directory["parent"] = current_directory["name"]
        current_directory["name"] += new_directory + "/"

def record_directory(command):

    """
        This method writes new directories to the dictionary.

        However this will overwrite the record of any directory with the 
        same name! FUCK!

        [X] :: Fixed by keeping track of path back to home. 

    """

    dir_to_append = command[4:]
    new_dir_name = current_directory["name"] + dir_to_append + "/"

    directories[new_dir_name] = {"name" : new_dir_name,
                             "parent" : current_directory["name"],
                             "files" : [],
                             "subdirectories" : [],
                             "size" : 0
                             }   

# This method will update the list of files using a file command.
def update_file(command):

    """
        Things that happen when new file found:

            [ ] :: Update the file system in the record of all directories.

        Note that file names are distinguished by not having $ or dir 
        at the beginning. 
    
        Command = 268495 jgfbgjdb


    """

    # Update in list of all directories.
    directories[current_directory["name"]]["files"].append(command)


# Now we can go through all the lines in the terminal readout
# and start to build up the dictionary of 
for line in terminal_readout:
    
    if line == "$ ls":
        pass

    elif line[:4] == "$ cd":
        # Change directory command.
        change_directory(line)
        
    elif line[:3] == "dir":
        # New directory
        record_directory(line)
        sub_dir = current_directory["name"] + line[4:] +"/"
        directories[current_directory["name"]]["subdirectories"].append(sub_dir)
        
    else:
        # Remaining line is a file. 
        update_file(line)
        
def file_size(file_name):

    return int(file_name.split(" ")[0])

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# With the directory structure stored, it remains to determine the size of 
# each directory. 

def update_directory_size(directory):

    # First account for the files in the immediate directory.
    files_in_directory = directories[directory]["files"]
    file_sum = 0
    for file in files_in_directory:
        
        file_sum += file_size(file)
    
    # Next account for files in subdirectories.
    # This works by recursively working down the branches of the tree.
    sub_directories = directories[directory]["subdirectories"]    
    sub_directory_total = 0
    for sub in sub_directories:
        sub_directory_total += update_directory_size(sub)
    
    return file_sum + sub_directory_total
    

for dir in directories.keys():
    directories[dir]["size"] = update_directory_size(dir)
    print("Directory " + directories[dir]["name"] + " has size " + str(directories[dir]["size"]))

answer = 0
for dir in directories.keys():
    if directories[dir]["size"] <= 100000:
        answer += directories[dir]["size"]

print(answer)

# ---------------------------------------------------------------------------
# ------------------------- Part Two ----------------------------------------
# ---------------------------------------------------------------------------

total_space_used = directories["/"]["size"]
difference = total_space_used - 30000000
print(difference)

min_sufficient_difference = 70000000
min_sufficient_directory = ""

for dir in directories.keys():

    dir_size = directories[dir]["size"]
    if (dir_size > difference) and (dir_size < min_sufficient_difference):
        min_sufficient_difference = dir_size
        min_sufficient_directory = directories[dir]
        print(min_sufficient_directory["name"])

print(min_sufficient_difference)
print(min_sufficient_directory)
# Incorrect Attempt 1 :: 31148261 /ltcqgnc/ [TOO BIG]


