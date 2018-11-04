import arcade
import random
from constants import BLOCK_SCALING, BLOCK_SIZE

# Generate map
def genMap():
    mapArray = list([])

    # Generate ground level
    for i in range (0, 10):
        mapArray.append([])
        for k in range(0, 100):
            mapArray[i].append(-1)

            if i == 6:
               mapArray[i][k] = 0
    
    mapArray[4 ][3] = 4 + 1
    
    # Add obstacles
    for i in range(0, 10):
        for k in range(0, 100):

            # Generate platforms and diamonds
            if k == random.randint(10, 90) and i < 4:
                mapArray[i][k] = 2
                mapArray[i - 2][k] = 5

            # Generate ground spikes and diamonds
            if k == (random.randint(10, 90) or random.randint(10, 90)) and i == (4 + 1):
                mapArray[i][k] = 4
                mapArray[i - 1][k - 2] = 2
                mapArray[i - 3][k] = 5
                
    
    return mapArray

def map(self):   
    map_array = genMap()

    for row_index, row in enumerate(map_array):
        for column_index, item in enumerate(row):

            # For this map, the numbers represent:
            # -1 = empty
            # 0  = grass block
            # 1  = dirt block
            # 2  = yellow brick
            # 3  = water block
            # 4  = floor spikes
            # 5  = blue diamond

            if item == -1:
                continue
            elif item == 0:
                wall = arcade.Sprite("images/grassBlock.png", BLOCK_SCALING)
            elif item == 1:
                wall = arcade.Sprite("images/dirtBlock.png", BLOCK_SCALING)
            elif item == 2:
                wall = arcade.Sprite("images/yellowBrick.png", BLOCK_SCALING)
            elif item == 3:
                wall = arcade.Sprite("images/waterTop.png", BLOCK_SCALING)
            elif item == 4:
                wall = arcade.Sprite("images/floorSpikes.png", BLOCK_SCALING)
                wall.right = column_index * BLOCK_SIZE * (6/5)
                wall.bottom = (6 - row_index) * BLOCK_SIZE
                self.enemy_list.append(wall)
            
                continue
            elif item == 5:
                wall = arcade.Sprite("images/blueDiamond.png", BLOCK_SCALING)
                wall.right = column_index * BLOCK_SIZE * (6/5)
                wall.bottom = (6 - row_index) * BLOCK_SIZE
                self.gems.append(wall)
                continue
            else:
                continue

            wall.right = column_index * BLOCK_SIZE * (6/5)
            wall.bottom = (6 - row_index) * BLOCK_SIZE
            self.wall_list.append(wall)