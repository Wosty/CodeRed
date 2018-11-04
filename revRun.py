import arcade
import random
from constants import *
import update
import setup

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
        setup.setup(self)

    def update(self, delta_time):
        update.update(self, delta_time)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()
        self.wall_list.draw()
        self.projectiles.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            self.proj = arcade.Sprite("images\\howdy.png", SPRITE_SCALING)
            self.proj.center_x = self.player_sprite._get_center_x()
            self.proj.center_y = self.player_sprite._get_center_y()+ 10
            self.proj.boundary_right = SPRITE_SIZE * 8
            self.proj.boundary_left = SPRITE_SIZE * 3
            self.proj.change_x = 2
            self.projectiles.append(self.proj)

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