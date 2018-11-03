import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class revRun(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("images\\rev.png", 0.1)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        for i in range(10):
            bevo = arcade.Sprite("images\\bevo.png", 0.1)

            bevo.center_x = random.randrange(SCREEN_WIDTH)
            bevo.center_y = random.randrange(SCREEN_HEIGHT)

            self.enemy_list.append(bevo)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()

    def update(self, delta_time):
        pass

def main():
    game = revRun(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()