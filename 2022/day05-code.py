# Advent of Code 2022 :: Day 05

# Read in the data 
data_file = open("day05-data.txt","r")
data_raw = data_file.read()
data_file.close()

data_raw = data_raw.split()

stacks_raw = data_raw[0]
instructions_raw = data_raw[1]



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

def crates_to_move(number_of_crates,stack):

    """
        Take "number_of_crates" from stack_one (list)
        and return that list in reverse. 


        3, [1,2,3,4,5,6] => [6,5,4]
    
    """

    top_crates = stack[-number_of_crates:]
    top_crates.reverse()

    return top_crates





