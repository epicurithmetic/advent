## Advent of Code 2022 :: Day 06
data_file = open("day06-data.txt","r")
data_raw = data_file.read()
data_file.close()
data = list(data_raw[:-1])

number_of_characters = 14 # Part Two: Change 4 to 14
length_of_message = len(data)
marker_found = False

current_four = data[:14] # Part Two: Change 4 to 14

while marker_found == False:

    if len(list(set(current_four))) == len(current_four):
        marker_found = True
        print(current_four)
        print(number_of_characters)
        
    else:
        current_four = current_four[1:] + list(data[number_of_characters])


    number_of_characters += 1

