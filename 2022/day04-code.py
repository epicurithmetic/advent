# Advent of Code 2022 :: Day 04

# Read in the data 
camp_sections_data_file = open("day04-data.txt","r")
camp_sections_data = camp_sections_data_file.read()
camp_sections_data_file.close()

# Split into pairs 
camp_pairs = camp_sections_data.split("\n")

total = 0

for pair in camp_pairs:

    pair = pair.split(",")

    i = 0
    while i < 2:
        pair[i] = pair[i].split("-")
        i+=1
    
    a = int(pair[0][0])
    b = int(pair[0][1]) + 1
    c = int(pair[1][0])
    d = int(pair[1][1]) + 1

    elf_one = set(range(a,b))
    elf_two = set(range(c,d))

    print(elf_one & elf_two)

    if not ((elf_one & elf_two) == set()):
        total += 1
    else:
        pass

print(total)