import arcade
import random
from constants import SPRITE_SCALING, BLOCK_SCALING, SCREEN_WIDTH, SPRITE_SIZE, BLOCK_SIZE, GRAVITY
from environment import genMap
import player

def setup(self):
    self.player_list = arcade.SpriteList()
    self.enemy_list = arcade.SpriteList()
    self.wall_list = arcade.SpriteList()
    self.projectiles = arcade.SpriteList()
    self.gems = arcade.SpriteList()

    player.player(self)

    map_array = genMap()

    #self.end_of_map = len(map_array[0]) * BLOCK_SIZE

    for row_index, row in enumerate(map_array):
        for column_index, item in enumerate(row):

            # For this map, the numbers represent:
            # -1 = empty
            # 0  = box
            # 1  = grass left edge
            # 2  = grass middle
            # 3  = grass right edge

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


    for i in range(3, 5):
        conflict = True
        while conflict:
            bevo = arcade.Sprite("images\\bevo.png", SPRITE_SCALING * 0.5)

            bevo.center_x = random.randrange(SCREEN_WIDTH) * (2 * i) + SCREEN_WIDTH
            bevo.bottom = 1.8 * BLOCK_SIZE

            #bevo.bottom = SPRITE_SIZE
            #bevo.left = SPRITE_SIZE * 2
            bevo.boundary_right = bevo.center_x + SPRITE_SIZE * 100
            bevo.boundary_left = bevo.center_x - SPRITE_SIZE * 100
            bevo.change_x = 2
            self.enemy_list.append(bevo)
            if len(arcade.check_for_collision_with_list(bevo, self.wall_list)) > 0 or len(arcade.check_for_collision_with_list(bevo, self.enemy_list)) > 1:
                self.enemy_list.remove(bevo)
            else:
                conflict = False

    for i in range(3, 5):
        conflict = True
        while conflict:
            mike = arcade.Sprite("images\\mike.png", SPRITE_SCALING * 1)
            
            mike.center_x = random.randrange(SCREEN_WIDTH) * ((2 * i) + 1) + SCREEN_WIDTH
            mike.bottom = 1.8 * BLOCK_SIZE
            
            # mike.bottom = SPRITE_SIZE
            # mike.left = SPRITE_SIZE * 2
            mike.boundary_right = mike.center_x + SPRITE_SIZE * 100
            mike.boundary_left = mike.center_x - SPRITE_SIZE * 100
            mike.change_x = 2
            self.enemy_list.append(mike)
            if len(arcade.check_for_collision_with_list(bevo, self.wall_list)) > 0 or len(arcade.check_for_collision_with_list(bevo, self.enemy_list)) > 1:
                self.enemy_list.remove(mike)
            else:
                conflict = False