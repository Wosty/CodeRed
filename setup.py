import arcade
import random
from constants import *
from environment import genMap

def setup(self):
    self.player_list = arcade.SpriteList()
    self.enemy_list = arcade.SpriteList()
    self.wall_list = arcade.SpriteList()
    self.projectiles = arcade.SpriteList()
    self.gems = arcade.SpriteList()

    self.score = 0
    self.texture_right = arcade.load_texture("images\\rev.png", mirrored=True, scale=SPRITE_SCALING)
    self.texture_left = arcade.load_texture("images\\rev.png", scale=SPRITE_SCALING)
    self.player_sprite = arcade.Sprite("images\\rev.png", SPRITE_SCALING)
    self.player_sprite.center_x = 400
    self.player_sprite.center_y = 300
    self.player_sprite.collision_radius -= 1000
    self.player_list.append(self.player_sprite)

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


    for i in range(1):
        bevo = arcade.Sprite("images\\bevo.png", SPRITE_SCALING)

        bevo.center_x = random.randrange(SCREEN_WIDTH)
        bevo.center_y = random.randrange(SCREEN_HEIGHT)

        #bevo.bottom = SPRITE_SIZE
        #bevo.left = SPRITE_SIZE * 2
        bevo.boundary_right = SPRITE_SIZE * 100
        bevo.boundary_left = -SPRITE_SIZE * 100
        bevo.change_x = 2
        self.enemy_list.append(bevo)

    for i in range(1):
        mike = arcade.Sprite("images\\mike.png", SPRITE_SCALING * 2)
        
        mike.center_x = random.randrange(SCREEN_WIDTH)
        mike.center_y = random.randrange(SCREEN_HEIGHT)
        
        # mike.bottom = SPRITE_SIZE
        # mike.left = SPRITE_SIZE * 2
        mike.boundary_right = SPRITE_SIZE * 100
        mike.boundary_left = -SPRITE_SIZE * 100
        mike.change_x = 2
        self.enemy_list.append(mike)

    #self.all_sprites = arcade.SpriteList()
    #self.all_sprites = self.enemy_list
    #self.all_sprites.append(self.player_sprite)

    #self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)        
    self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, gravity_constant=GRAVITY)        
    #self.physics_engine = arcade.PhysicsEnginePlatformer(self.all_sprites, self.wall_list, gravity_constant=GRAVITY)