import arcade
import random
from constants import JUMP_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, MOVEMENT_SPEED, SPRITE_SCALING, SPRITE_SIZE
import update
import setup

class revRun(arcade.Window):
    """ Main application class. """

    #Initialize variables
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.wall_list = None
        self.player_list = None
        self.enemy_list = None
        self.projectiles = None
        self.gems = None

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
        self.gems.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, self.view_left+10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE and self.score < 0:
            self.proj = arcade.Sprite("images\\howdy.png", SPRITE_SCALING * 2)
            self.proj.center_x = self.player_sprite._get_center_x()
            self.proj.center_y = self.player_sprite._get_center_y()+ 10
            self.proj.boundary_right = self.proj.center_x + SPRITE_SIZE * 100
            self.proj.boundary_left = self.proj.center_x - SPRITE_SIZE * 100
            if self.player_sprite.texture == self.texture_left:
                self.proj.change_x = -10
            else:
                self.proj.change_x = 10
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