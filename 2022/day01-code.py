# Retrieve data. 
elf_calories_file = open("day01-data.txt","r")
elf_calories = elf_calories_file.read()
elf_calories_file.close()

# Split on double newline \n\n to get a list of separate elves. 
list_of_elves = elf_calories.split("\n\n")

# Clean the data up some.
number_of_elves = len(list_of_elves)

for i in range(number_of_elves):

    list_of_elves[i] = list_of_elves[i].split("\n")

# Obtain the maximum number of calories
total_calories = 0
i = 0
while i < 3:

    # Cycle through the list three times: searching for and removing the 
    # elf with the most calories each time. 

    # Keep track of the total calories at the end of each cycle. 

    # Would be nicer to order the list by number of calories. But we are only 
    # looking for three elves: so this won't take long.

    max_calories = 0
    max_elf = 0

    for j in range(len(list_of_elves)):

        elf_calories = 0

        for food_item in list_of_elves[j]:
            if food_item == '':
                pass
            else:
                elf_calories += int(food_item)
        
        if elf_calories > max_calories:
            max_calories = elf_calories
            max_elf = j
        else:
            pass
    
    # Update the total number of calories. 
    total_calories += max_calories

    # Remove that elf from the list.
    del list_of_elves[max_elf] 

    # Increment counter to get the elf with the next most calories. 
    i += 1

# Answer is: 
print(total_calories)



