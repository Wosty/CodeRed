import arcade
from constants import SPRITE_SCALING, GRAVITY, BLOCK_SIZE, SPRITE_SIZE

# Spawn player entity
def player(self):

    # Create player sprite
    self.texture_right = arcade.load_texture("images\\rev.png", mirrored=True, scale=SPRITE_SCALING)
    self.texture_left = arcade.load_texture("images\\rev.png", scale=SPRITE_SCALING)
    self.player_sprite = arcade.Sprite("images\\rev.png", SPRITE_SCALING)

    # Sets center for player sprite
    self.player_sprite.center_x = self.view_left - SPRITE_SIZE
    self.player_sprite.center_y = BLOCK_SIZE * 1.5

    # Sprite list for plyaer entity
    self.player_list.append(self.player_sprite)
    self.player_list.update()

    # Create physics for player entity
    self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, gravity_constant=GRAVITY)
