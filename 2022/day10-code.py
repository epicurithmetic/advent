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

# ------------------------------------------------------
# Part One :: Complete
# ------------------------------------------------------

# for instruction in instructions_raw:

#     print(register_X, register_X % 40)

#     if instruction == "noop":
        
#         # Tick-tock.
#         number_of_cycles += 1

#         # Check the cycle and register.
#         signal_strength = number_of_cycles*register_X

#         number_of_instructions += 1

#         if number_of_cycles in cycles_to_check:
#             print(number_of_instructions,number_of_cycles,register_X,signal_strength)
#             signal_strength_checks.append(signal_strength)

#     else:
#         # In this case the register is updated. 
#         instruction_list = instruction.split(" ")
#         update_amount = int(instruction_list[1])

#         number_of_instructions += 1

#         # Tick...
#         number_of_cycles += 1

#         # Check the cycle and register.
 
#         signal_strength = number_of_cycles*register_X

#         if number_of_cycles in cycles_to_check:
#             print(number_of_instructions,number_of_cycles,register_X,signal_strength)
#             signal_strength_checks.append(signal_strength)
                
#         # ... tock.
#         number_of_cycles += 1

#         # Update the register.
#         register_X += update_amount
                   

#         # -----------------------------------------------------
#         # PART ONE: STUFF
#         # -----------------------------------------------------
#         # Check the cycle and register.
#         signal_strength = number_of_cycles*register_X

#         if number_of_cycles in cycles_to_check:
#             print(number_of_instructions,number_of_cycles,register_X,signal_strength)
#             signal_strength_checks.append(signal_strength)

# for element in signal_strength_checks:
#     print(element)

# print(sum(signal_strength_checks))        



# ------------------------------------------------------------------
#               Part Two :: Screen Readout
# ------------------------------------------------------------------

# Start the sprite centered on 1 i.e. covering 0,1,2
sprite_center = 1

# Keep track of how far along we are printing. 
pixel_to_print = 0
screen = []
row_of_pixels = 0

end_row_list = [41,81,121,161,201,241]
row = []

for instruction in instructions_raw:

    # If instruction is noop
    # [ ] :: Draw the pixel.
    # [ ] :: Update pixel to draw. Check row.
    # [ ] :: Cycle the clock.
    if instruction == "noop":
                
        if sprite_center-1 <= pixel_to_print <= sprite_center+1:
            row.append("#")
            pixel_to_print = (pixel_to_print + 1) % 40
        else:
            row.append(".")
            pixel_to_print = (pixel_to_print + 1) % 40

        # Tick            
        number_of_cycles += 1
        
        # Check if row complete. Move accordingly. 
        if number_of_cycles in end_row_list:
            screen.append(row)
            row = []
        else:
            pass

        # Update instruction count
        number_of_instructions += 1

    # else the instruction is an addx n
    # [ ] :: Draw pixel 
    # [ ] :: Update pixel to draw. Check row.
    # [ ] :: Cycle the clock.
    # [ ] :: Draw pixel. 
    # [ ] :: Update pixel to draw. Check row.
    # [ ] :: Update register
    # [ ] :: Update sprite center. 
    # [ ] :: Cycle the clock.

    else:
        
        # Draw the first pixel.
        if sprite_center-1 <= pixel_to_print <= sprite_center+1:
            row.append("#")
            pixel_to_print = (pixel_to_print + 1) % 40
        else:
            row.append(".")
            pixel_to_print = (pixel_to_print + 1) % 40
        
        # Tick
        number_of_cycles += 1
        
        # Check if row complete. Move accordingly. 
        if number_of_cycles in end_row_list:
            screen.append(row)
            row = []
        else:
            pass

       # Draw the second pixel.
        if sprite_center-1 <= pixel_to_print <= sprite_center+1:
            row.append("#")
            pixel_to_print = (pixel_to_print + 1) % 40
        else:
            row.append(".")
            pixel_to_print = (pixel_to_print + 1) % 40
        
        # Tick
        number_of_cycles += 1
                
        # Check if row complete. Move accordingly. 
        if number_of_cycles in end_row_list:
            screen.append(row)
            row = []
        else:
            pass        
        
        # In this case the register is updated. 
        instruction_list = instruction.split(" ")
        update_amount = int(instruction_list[1])

        # Update the register.
        register_X += update_amount
        sprite_center = (sprite_center + update_amount) % 40

print("Screen Readout :: ")

for row in screen:
    
    row_string = ""
    for pixel in row:
        row_string += pixel
    
    print(row_string, len(row_string))




































