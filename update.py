import arcade
from constants import SPRITE_SCALING, SCREEN_WIDTH, SCREEN_HEIGHT, VIEWPORT_MARGIN, RIGHT_MARGIN, MOVEMENT_SPEED, BLOCK_SIZE, WIN_SCORE, SPRITE_SIZE
import player
import level
import time

def update(self, delta_time):

    self.enemy_list.update()
    self.projectiles.update()
    #self.badProjectiles.update()

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
    
    # for proj in self.badProjectiles:
    #     # If the enemy hit a wall, reverse
    #     if len(arcade.check_for_collision_with_list(proj, self.wall_list)) > 0 or len(arcade.check_for_collision_with_list(proj, self.enemy_list)) > 1:
    #         proj.kill()
    #     # If the enemy hit the left boundary, reverse
    #     elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
    #         proj.kill()
    #     # If the enemy hit the right boundary, reverse
    #     elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
    #         proj.kill()

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
    
    # if self.score > WIN_SCORE / 2 and time.time() % 10 < 1 and time.time() - self.timer > 5:
    #     for enemy in self.enemy_list:
    #         self.proj = arcade.Sprite("images\\howdy.png", SPRITE_SCALING * 10)
    #         self.proj.center_x = enemy._get_center_x()
    #         self.proj.center_y = enemy._get_center_y() + 10
    #         self.proj.boundary_right = self.proj.center_x + SPRITE_SIZE * 100
    #         self.proj.boundary_left = self.proj.center_x - SPRITE_SIZE * 100
    #         if self.player_sprite._get_center_x() < enemy._get_center_x():
    #             self.proj.change_x = -2
    #             self.proj.change_angle = -5
    #         else:
    #             self.proj.change_x = 2
    #             self.proj.change_angle = 5
    #         self.badProjectiles.append(self.proj)
    #     self.timer = time.time()
    #     self.badProjectiles.update()
        

    hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)

    if len(hit_list) > 0:
        self.score -= 1
        self.player_sprite.kill()
        player.player(self)

    # hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.badProjectiles)

    # if len(hit_list) > 0:
    #     self.score -= 1
    #     self.player_sprite.kill()
    #     for dead in hit_list:
    #         dead.kill()
    #     player.player(self)

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