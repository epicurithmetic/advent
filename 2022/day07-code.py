# Advent of Code 2022 :: Day 07

# Read in the data from terminal. 
terminal_file = open("day07-testData.txt","r")
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
            "subdirectories" : []}
            }

# This dictionary keeps track of current place in file system.
current_directory = {
    "name" : "/",
    "parent" : None,
    }

# This method uses a cd command to change the current directory
# while also checking to see if the directory dictionary needs updating.
def change_directory(command):

    """
        Things that happen when cd command made:

            [ ] :: Change the current directory.
            [ ] :: Update the directory list. 
    
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
        current_directory["name"] = new_directory




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
    directories[current_directory["name"]]["subdirectories"].append(command)




