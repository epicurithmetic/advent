# Advent of Code 2022 :: Day 10
instructions_file = open("day10-data.txt","r")
intructions_raw = instructions_file.read()
instructions_file.close()
instructions_raw = intructions_raw.split("\n")

# Initialise counters
register_X = 1
number_of_cycles = 1
signal_strength_checks = []
cycles_to_check = [20,60,100,140,180,220]
number_of_instructions = 0

# Part One :: Complete
for instruction in instructions_raw:

    if instruction == "noop":

        number_of_cycles += 1

        # Check the cycle and register.
        signal_strength = number_of_cycles*register_X

        number_of_instructions += 1

        if number_of_cycles in cycles_to_check:
            print(number_of_instructions,number_of_cycles,register_X,signal_strength)
            signal_strength_checks.append(signal_strength)

        
        

    else:
        # In this case the register is updated. 
        instruction_list = instruction.split(" ")
        print(instruction)
        update_amount = int(instruction_list[1])

        number_of_instructions += 1

        # Tick...
        number_of_cycles += 1

        # Check the cycle and register.
        signal_strength = number_of_cycles*register_X

        if number_of_cycles in cycles_to_check:
            print(number_of_instructions,number_of_cycles,register_X,signal_strength)
            signal_strength_checks.append(signal_strength)
        
        # Update the register.
        register_X += update_amount
        
        # ... tock.
        number_of_cycles += 1

        # Check the cycle and register.
        signal_strength = number_of_cycles*register_X

        if number_of_cycles in cycles_to_check:
            print(number_of_instructions,number_of_cycles,register_X,signal_strength)
            signal_strength_checks.append(signal_strength)

for element in signal_strength_checks:
    print(element)

print(sum(signal_strength_checks))        