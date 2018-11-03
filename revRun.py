import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class revRun(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite(".png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        arcade.finish_render()

    def update(self, delta_time):
        pass

def main():
    game = revRun(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()