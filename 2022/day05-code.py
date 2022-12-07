# Advent of Code 2022 :: Day 05

# Read in the data 
data_file = open("day05-data.txt","r")
data_raw = data_file.read()
data_file.close()
data_raw = data_raw.split("\n\n")

# Clean up the stacks data.
stacks_raw = data_raw[0]
stacks_raw = stacks_raw.split("\n")
stacks_raw = stacks_raw[:-1] # Remove the line 1 2 3 4 ... 
stacks_raw.reverse()

# Initialise stacks array.
number_of_stacks = 9
stacks = []
i = 0
while i < 9: 
    stacks.append([])
    i += 1

# Parse data to get crates into the stacks array.
number_of_levels = len(stacks_raw)
level = 0 
while level < number_of_levels:    
    # For each level we need to seek through each stack.
    stack = 0
    while stack < 9:
        crate = stacks_raw[level][:4]
        stacks_raw[level] = stacks_raw[level][4:]
        
        # If the crate is empty, then don't append. 
        if not (crate == "    " or crate == "   "):
            stacks[stack].append(crate)

        stack += 1
    level += 1

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

# Do the moving
for instruction in instructions:
    
    number_to_move = instruction[0]
    from_stack = instruction[1]-1
    to_stack = instruction[2]-1

    # Pick out the crates and remove them from from_stack.
    crates = stacks[from_stack][-number_to_move:]
    stacks[from_stack] = stacks[from_stack][:-number_to_move]

    # Part Two just required this line to be commented out. 
    #crates.reverse()  

    # Add crates on the end of to_stack.
    stacks[to_stack] = stacks[to_stack] + crates

# Print the top of each stack.
for stack in stacks:
    print(stack[-1])