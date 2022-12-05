# Advent of Code 2022 :: Day 05

# Read in the data 
data_file = open("day05-data.txt","r")
data_raw = data_file.read()
data_file.close()
data_raw = data_raw.split("\n\n")

# Clean up the stacks data.
stacks_raw = data_raw[0]
stacks_raw = stacks_raw.split("\n")
stacks_raw = [:-1] # Remove the line 1 2 3 4 ... 

stacks = [[],[],[],
           [],[],[],
           [],[],[]]


#for row in stacks_raw:
    # i = 0
    # while i < 9:
        #stacks[i] = row[i:i+4]






# Clean up the instructions data.
def extract_instruction(raw_instruction):

    """
        Take string of form: 

        move 5 from 3 to 6

        return list [5,3,6]
    
    """

    raw_instruction = raw_instruction.split(" ")
    raw_instruction.remove("move")
    raw_instruction.remove("from")
    raw_instruction.remove("to")

    instruction = [int(x) for x in raw_instruction]

    return instruction


# Use this method to clean up the instructions. 
instructions_raw = data_raw[1]
instructions_raw = instructions_raw.split("\n")
instructions = [extract_instruction(x) for x in instructions_raw]

# Method to grab the crates from a stack ready to append to another stack.
def crates_to_move(number_of_crates,stack):

    """
        Take "number_of_crates" from stack_one (list)
        and return that list in reverse. 


        3, [1,2,3,4,5,6] => [6,5,4]
    
    """

    # Grab the crates.
    top_crates = stack[-number_of_crates:]
    # Reverse them to get the correct order: crane takes one at a time. 
    top_crates.reverse()

    return top_crates





