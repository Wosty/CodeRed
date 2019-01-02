import arcade
import pygame
import random
from constants import SPRITE_SCALING, BLOCK_SCALING, SCREEN_WIDTH, SPRITE_SIZE, BLOCK_SIZE, GRAVITY
import player
import level

def enemies(self):
    for i in range(random.randint(3, 5)):
        conflict = True
        while conflict:
            bevo = arcade.Sprite("images\\bevo.png", SPRITE_SCALING * 0.75)

            bevo.center_x = self.player_sprite.center_x + ((random.randrange(100) / 100.0) + ((2 * i) + 1) + 2) * SCREEN_WIDTH
            bevo.bottom = 1.8 * BLOCK_SIZE

            #bevo.bottom = SPRITE_SIZE
            #bevo.left = SPRITE_SIZE * 2
            bevo.boundary_right = bevo.center_x + SPRITE_SIZE * 100
            bevo.boundary_left = bevo.center_x - SPRITE_SIZE * 100
            bevo.change_x = 2
            self.enemy_list.append(bevo)
            if len(arcade.check_for_collision_with_list(bevo, self.wall_list)) > 0 or len(arcade.check_for_collision_with_list(bevo, self.enemy_list)) > 1:
                self.enemy_list.remove(bevo)
            else:
                conflict = False

    for i in range(0, random.randint(3, 5)):
        conflict = True
        while conflict:
            mike = arcade.Sprite("images\\mike.png", SPRITE_SCALING * 1.25)
            
            mike.center_x = self.player_sprite.center_x + ((random.randrange(100) / 100.0) + ((2 * i) + 1) + 2) * SCREEN_WIDTH
            mike.bottom = 1.5 * BLOCK_SIZE
            
            # mike.bottom = SPRITE_SIZE
            # mike.left = SPRITE_SIZE * 2
            mike.boundary_right = mike.center_x + SPRITE_SIZE * 100
            mike.boundary_left = mike.center_x - SPRITE_SIZE * 100
            mike.change_x = 2
            self.enemy_list.append(mike)
            if len(arcade.check_for_collision_with_list(bevo, self.wall_list)) > 0 or len(arcade.check_for_collision_with_list(bevo, self.enemy_list)) > 1:
                self.enemy_list.remove(mike)
            else:
                conflict = False

def setup(self):
    self.player_list = arcade.SpriteList()
    self.enemy_list = arcade.SpriteList()
    self.wall_list = arcade.SpriteList()
    self.projectiles = arcade.SpriteList()
    self.badProjectiles = arcade.SpriteList()
    self.gems = arcade.SpriteList()
    self.edge = BLOCK_SIZE     # I hope changing this to 1 fixes everything
    self.win  = False
    self.timer = 0

    # Setup pygame and play Aggie War Hymn
    #pygame.init()
    #pygame.mixer.init()
    #pygame.mixer.music.load(WAR_HYMN)
    #pygame.mixer.music.play()

    player.player(self)
    level.map(self)
    enemies(self)