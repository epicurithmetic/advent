# Advent of Code 2022 :: Day 03

# For use later. 
alphabet = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))

# Read in the data 
rucksacks_data_file = open("day03-data.txt","r")
rucksacks_data = rucksacks_data_file.read()
rucksacks_data_file.close()

rucksacks_data = rucksacks_data.split("\n")

# Organise the rucksacks into their compartments.
rucksacks = []
for sack in rucksacks_data:

    #print(sack)
    length_of_sack = len(sack)//2
    
    compartment_one = sack[:length_of_sack]
    compartment_two = sack[length_of_sack:]

    rucksacks.append([compartment_one,compartment_two])

# Search for the repeated item. Get the priority.
sum_of_priorities = 0

for sack in rucksacks:

    compartment_one = list(sack[0])
    compartment_two = list(sack[1])


    # Look for the repeated item.
    repeated_item = ""

    for item in compartment_one:
        for other_item in compartment_two:

            if item == other_item:
                repeated_item = item
    
    sum_of_priorities += alphabet.index(repeated_item) + 1

# Back to rucksacks data. Get them in their groups of three.
number_of_groups = len(rucksacks_data) // 3
groups = []
i = 0
while i < number_of_groups:
    lower = i*3
    upper = i*3 + 3
    group = rucksacks_data[lower:upper]
    groups.append(group)
    i+=1

# initialise badge priorities
badge_priorities = 0

# Find the badge character for each group. 
for group in groups:

    badge_character = ""
    
    elf_sack_one = group[0]
    elf_sack_two = group[1]
    elf_sack_three = group[2]

    # Compare elf_one with elf_two.
    # If something in common, then check elf_three for it.
    for item_one in elf_sack_one:
        for item_two in elf_sack_two:

            if item_one == item_two:
                for item_three in elf_sack_three:
                    if item_one == item_three:
                        badge_character = item_one
                    else:
                        pass                        
            else:
                pass
    
    badge_priorities += (1 + alphabet.index(badge_character))

print(badge_priorities)





    