# Advent of Code 2022 :: Day 08

# Read the data
forest_raw_file = open("day08-data.txt","r")
forest_raw = forest_raw_file.read()
forest_raw_file.close()

# Clean the trees up some. 
forest_raw = forest_raw.split("\n")
forest = []
for row in forest_raw:
    forest.append(list(row))

number_of_rows = len(forest)
number_of_columns = len(forest[0])

number_of_visible_trees = 2*number_of_rows + 2*number_of_columns - 4

# Check the interior trees.
for i in range(1,number_of_rows-1):
    for j in range(1,number_of_columns-1):
       
        # Tree
        tree = int(forest[i][j])
        
        # Tree in row and column:
        row = [int(x) for x in forest[i]]
        column = [int(forest[x][j]) for x in range(number_of_rows)]

        # Check if tallest in row.
        left = row[:j]
        right = row[j+1:]

        visible_left = True
        visible_right = True

        # Look left
        for other_tree in left:
            visible_left = visible_left and (tree > other_tree)
        
        # Look left
        for other_tree in right:
            visible_right = visible_right and (tree > other_tree)
        
        visible_along_row = visible_left or visible_right

        # Check if tallest in column
        up = column[:i]
        down = column[i+1:]

        visible_up = True
        visible_down = True

        # Look up 
        for other_tree in up:
            visible_up = (visible_up and (tree > other_tree))
        
        # Look down
        for other_tree in down:
            visible_down = (visible_down and (tree > other_tree))
        
        visible_along_column = visible_up or visible_down

        # Can outsides see the tree?
        visible = visible_along_row or visible_along_column

        if visible:
            number_of_visible_trees += 1

print("There are ", number_of_visible_trees, " trees visible from the edge of the forest.")

# ---------------------------------------------------------------------------
# ------------------------- Part Two ----------------------------------------
# ---------------------------------------------------------------------------

max_scenic_score = 1

# Check the interior trees. Edge trees have scenic_score = 0
for i in range(1,number_of_rows-1):
    for j in range(1,number_of_columns-1):

        # Grab tree.
        tree = int(forest[i][j])
        
        # Tree in row and column:
        row = [int(x) for x in forest[i]]
        column = [int(forest[x][j]) for x in range(number_of_rows)]

        # Determine the neighbourhood of tree.
        left = row[:j]
        left.reverse()
        right = row[j+1:]
        up = column[:i]
        up.reverse()
        down = column[i+1:]

        # Look in each direction to determine the scenic_score of the tree.
        directions = [left,right,up,down]
        scenic_score = 1

        for direction in directions:

            viewing_distance = 0    
            view_blocked = False
            number_tree_in_direction = 0

            while not view_blocked:
                if tree <= direction[number_tree_in_direction]:
                    view_blocked = True
                    viewing_distance += 1

                elif tree > direction[number_tree_in_direction]:
                    viewing_distance += 1
                    number_tree_in_direction += 1
                
                if number_tree_in_direction == len(direction):
                    view_blocked = True

            scenic_score *= viewing_distance
            
        if scenic_score >= max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)

# Incorrect Attempt 1 :: 3130512 [Too large]
# Correct Answer      :: 479400
        





        

        



