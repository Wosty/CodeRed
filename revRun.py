import arcade
import random
from environment import *

SPRITE_SCALING = 0.1
BLOCK_SCALING = SPRITE_SCALING * 15

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

SPRITE_PIXEL_SIZE = 52
SPRITE_SIZE = int(SPRITE_PIXEL_SIZE * SPRITE_SCALING)
BLOCK_SIZE = int(SPRITE_PIXEL_SIZE * BLOCK_SCALING)

VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 150

MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 0.5

class revRun(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.wall_list = None
        self.player_list = None

        self.score = 0
        self.player_sprite = None

        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0
        self.texture_right = arcade.load_texture("images\\rev.png", mirrored=True, scale=SPRITE_SCALING)
        self.texture_left = arcade.load_texture("images\\rev.png", scale=SPRITE_SCALING)
        self.player_sprite = arcade.Sprite("images\\rev.png", SPRITE_SCALING)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
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
                else:
                    continue

                wall.right = column_index * 64
                wall.top = (7 - row_index) * 64
                self.wall_list.append(wall)


        # for i in range(1):
        #     bevo = arcade.Sprite("images\\bevo.png", SPRITE_SCALING)

        #     bevo.center_x = random.randrange(SCREEN_WIDTH)
        #     bevo.center_y = random.randrange(SCREEN_HEIGHT)

        #     bevo.bottom = SPRITE_SIZE
        #     bevo.left = SPRITE_SIZE * 2

        #     self.enemy_list.append(bevo)

        # for i in range(1):
        #     mike = arcade.Sprite("images\\mike.png", SPRITE_SCALING)
            
        #     mike.center_x = random.randrange(SCREEN_WIDTH)
        #     mike.center_y = random.randrange(SCREEN_HEIGHT)
            
        #     mike.bottom = SPRITE_SIZE
        #     mike.left = SPRITE_SIZE * 2
            
        #     self.enemy_list.append(mike)

        #self.all_sprites = arcade.SpriteList()
        #self.all_sprites = self.enemy_list
        #self.all_sprites.append(self.player_sprite)

        #self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, gravity_constant=GRAVITY)        
        #self.physics_engine = arcade.PhysicsEnginePlatformer(self.all_sprites, self.wall_list, gravity_constant=GRAVITY)


    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()
        self.wall_list.draw()

    def update(self, delta_time):
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)

        if len(hit_list) > 0:
            self.player_sprite.kill()

        if self.player_sprite.change_x < 0:
            self.player_sprite.texture = self.texture_left
        if self.player_sprite.change_x > 0:
            self.player_sprite.texture = self.texture_right

        changed = False

        # Scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left, self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    game = revRun(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()