# Advent of Code 2022 :: Day 09
head_movements_file = open("day09-data.txt","r")
head_movements = head_movements_file.read()
head_movements_file.close()
head_movements = head_movements.split("\n")
head_movements = head_movements[:-1]


class snake:

    def __init__(self,head_x,head_y,tail_x,tail_y):

        self.headX = head_x
        self.headY = head_y
        self.tailX = tail_x
        self.tailY = tail_y

        self.tailPositions = [(tail_x,tail_y)]

        self.sepHeadTail_x = abs(self.headX - self.tailX)
        self.sepHeadTail_y = abs(self.headY - self.tailY)
    
    def updateSep(self):

        self.sepHeadTail_x = abs(self.headX - self.tailX)
        self.sepHeadTail_y = abs(self.headY - self.tailY)


    def motion(self,instruction):

        instruction = instruction.split(" ")

        direction = instruction[0]
        distance_to_move = int(instruction[1])
        distance_moved = 0

        while distance_moved < distance_to_move:

            # Update the head position.
            if direction == "R":
                self.headX += 1
            elif direction == "L":
                self.headX -= 1
            elif direction == "U":
                self.headY += 1
            else:
                self.headY -= 1
            
            self.updateSep()

            # Now update the tail position accordingly.
            if (self.sepHeadTail_x <= 1) and (self.sepHeadTail_y <= 1):
                # In this case, the tail is still touching, so do nothing. 
                print("Tail not moving")
                print(self.headX,self.tailX,(self.headX - self.tailX),(self.sepHeadTail_y <= 1))
                pass
            else:
                # In this case, tail needs to move. 
                # We can use direction to say where. 
                if direction == "R":
                    # If the head has moved to the right, 
                    # then the tail will fall in behind it. 
                    self.tailX = self.headX - 1
                    self.tailY = self.headY

                elif direction == "L":
                    self.tailX = self.headX + 1
                    self.tailY = self.headY
                    
                elif direction == "U":
                    self.tailX = self.headX
                    self.tailY = self.headY-1             
                    
                else:
                    self.tailX = self.headX
                    self.tailY = self.headY+1
                    
            distance_moved += 1
            self.tailPositions.append((self.tailX,self.tailY))
            #print(self.tailPositions)
            #print("Slithering", distance_moved)
        
        print(self.headX,self.tailX)

elf_snake = snake(0,0,0,0)

for movement in head_movements:
    elf_snake.motion(movement)

print(len(set(elf_snake.tailPositions)))