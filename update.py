import arcade
from constants import SPRITE_SCALING, SCREEN_WIDTH, SCREEN_HEIGHT, VIEWPORT_MARGIN, RIGHT_MARGIN, MOVEMENT_SPEED, BLOCK_SIZE
import player
import level

def update(self, delta_time):

    self.enemy_list.update()
    self.projectiles.update()

    # Spooky math to get edge of level
    if self.player_sprite.center_x > self.edge - SCREEN_WIDTH - 10:
        level.map(self)

    # Check each enemy
    for enemy in self.enemy_list:
        # If the enemy hit a wall, reverse
        if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0 or len(arcade.check_for_collision_with_list(enemy, self.enemy_list)) > 1:
            enemy.change_x *= -1
        # If the enemy hit the left boundary, reverse
        elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
            enemy.change_x *= -1
        # If the enemy hit the right boundary, reverse
        elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
            enemy.change_x *= -1

    for proj in self.projectiles:
        if len(arcade.check_for_collision_with_list(proj, self.wall_list)) > 0:
            proj.kill()
        elif len(arcade.check_for_collision_with_list(proj, self.enemy_list)) > 0:
            for dead in arcade.check_for_collision_with_list(proj, self.enemy_list):
                dead.kill()
            self.score += 1
        elif proj.boundary_left is not None and proj.left < proj.boundary_left:
            proj.kill()
        elif proj.boundary_right is not None and proj.right > proj.boundary_right:
            proj.kill()

    hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)

    if len(hit_list) > 0:
        self.score -= 1
        self.player_sprite.kill()
        player.player(self)

    hit_gem = arcade.check_for_collision_with_list(self.player_sprite, self.gems)
    self.score += (len(hit_gem) * 5)
    for gem in hit_gem:
        gem.kill()

    if self.player_sprite.change_x < 0:
        self.player_sprite.texture = self.texture_left
    if self.player_sprite.change_x > 0:
        self.player_sprite.texture = self.texture_right

    changed = False

    # Scroll left
    left_bndry = self.view_left + VIEWPORT_MARGIN
    if self.player_sprite.left < left_bndry:
        self.player_sprite.change_x = MOVEMENT_SPEED
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