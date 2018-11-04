import arcade
import random

SPRITE_SCALING = 0.1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)

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

        self.player_sprite = arcade.Sprite("images\\rev.png", SPRITE_SCALING)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        for i in range(5):
            bevo = arcade.Sprite("images\\bevo.png", SPRITE_SCALING)

            bevo.center_x = random.randrange(SCREEN_WIDTH)
            bevo.center_y = random.randrange(SCREEN_HEIGHT)

            self.enemy_list.append(bevo)

        for i in range(10):
            mike = arcade.Sprite("images\\mike.png", SPRITE_SCALING)

            mike.center_x = random.randrange(SCREEN_WIDTH)
            mike.center_y = random.randrange(SCREEN_HEIGHT)

            self.enemy_list.append(mike)

        self.all_sprites = arcade.SpriteList()
        self.all_sprites = self.enemy_list
        self.all_sprites.append(self.player_sprite)
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.all_sprites, self.wall_list, gravity_constant=GRAVITY)


    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()
        self.wall_list.draw()

    def update(self, delta_time):
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.player_list)

        if len(hit_list) < 0:
            self.player_sprite.kill()

        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED

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