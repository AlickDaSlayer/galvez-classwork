import pygame as pg
import sys
import random
from maps import map1, map2

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
LIME = (100, 255, 100)

pg.init()

# Set the width and height of the screen [width, height]
size = (1400, 720)
screen = pg.display.set_mode(size)

font1 = pg.font.SysFont(None, 200)
font2 = pg.font.SysFont(None, 100)
font3 = pg.font.SysFont(None, 20)

pg.display.set_caption("Block Charge")

all_sprites_group = pg.sprite.Group()

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, colour, w, h):
        super().__init__()
        self.image = pg.Surface([w,h])
        self.image.fill(colour)
        # Set the position of the player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left_pressed = False
        self.right_pressed = False
        self.down_pressed = False
        self.up_pressed = False
        self.speed = 5

    def update(self):
        self.velX = 0
        self.velY = 0

        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.rect.x += self.velX
        self.rect.y += self.velY

player = Player(500, 400, GREEN, 20, 20)
all_sprites_group.add(player)

class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, colour, w, h):
        super().__init__()
        self.image = pg.Surface([w,h])
        self.image.fill(colour)
        # Set the position of the player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left_pressed = False
        self.right_pressed = False
        self.down_pressed = False
        self.up_pressed = False
        self.chance_x = random.randint(1,2)
        self.chance_y = random.randint(1,2)
        self.speed = 1

    def update(self):
        if self.chance_x == 1:
            self.rect.x += self.speed
        elif self.chance_x == 2:
            self.rect.x -= self.speed
        if self.chance_y == 1:
            self.rect.y += self.speed
        elif self.chance_y == 2:
            self.rect.y -= self.speed

        col = pg.sprite.spritecollide(self, wall_group, False)
        for i in col:
            self.speed = self.speed * -1
            self.chance_x = random.randint(1, 2)
            self.chance_y = random.randint(1, 2)

enemy_group = pg.sprite.Group()

class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, colour, w, h):
        super().__init__()
        self.image = pg.Surface([w,h])
        self.image.fill(colour)
        # Set the position of the player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


wall_group = pg.sprite.Group()


class Sword(pg.sprite.Sprite):
    def __init__(self, x, y, colour, w, h):
        super().__init__()
        self.image = pg.Surface([w,h])
        self.image.fill(colour)
        # Set the position of the player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = None
        self.counter = 0

    #def update(self):
        #if self.counter is not None:
            #if self.counter == 800:


    #def update(self):
        #if self.time is not None:
            #if pg.time.get_ticks() - self.time >= 10:
                #all_sprites_group.remove(self)


sword_group = pg.sprite.Group()

def draw_map(map):
    x = 0
    y = 0

    for row in map:
        for col in row:
            if col == 1:
                my_wall = Wall(x, y, RED, 20, 20)
                wall_group.add(my_wall)
            x += 20
        x = 0
        y += 20

def levels():
    draw_map(map1)

    enemy_number = 8
    spawnPositions_x = [0,0,0,0,0,0,0,0]
    for i in range(enemy_number):
        spawnPositions_x[i] = random.randint(15, 1230)
    spawnPositions_y = [0,0,0,0,0,0,0,0]
    for i in range(enemy_number):
        spawnPositions_y[i] = random.randint(15, 675)

    for i in range(enemy_number):
        my_enemy = Enemy(spawnPositions_x[i], spawnPositions_y[i], LIME, 40, 40)
        enemy_group.add(my_enemy)
        all_sprites_group.add(my_enemy)

# Used to manage how fast the screen updates
clock = pg.time.Clock()

def draw_text(text, font, colour, surface, x, y):
    text_obj = font.render(text, 1, colour)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    textrect_pos = screen.blit(text_obj, text_rect)

def main_menu():
    while True:

        screen.fill(BLACK)
        draw_text("Main Menu", font1, BLUE, screen, 290, 100)

        mx, my = pg.mouse.get_pos()

        button_1 = pg.Rect(500, 305, 390, 100)
        button_2 = pg.Rect(500, 505, 390, 100)
        pg.draw.rect(screen, BLUE, button_1)
        pg.draw.rect(screen, BLUE, button_2)
        draw_text("Start Game", font2, WHITE, screen, 510, 320)
        draw_text("Credits", font2, WHITE, screen, 560, 520)

        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                credits()

        pg.display.update()
        clock.tick(60)

def credits():
    while True:
        screen.fill(BLACK)
        draw_text("Made by:", font1, WHITE, screen, 290, 100)
        draw_text("Alick Galvez", font1, WHITE, screen, 290, 300)

        mx, my = pg.mouse.get_pos()

        button_exit = pg.Rect(25, 25, 175, 75)
        pg.draw.rect(screen, BLUE, button_exit)
        draw_text("Back", font2, WHITE, screen, 28, 28)

        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_exit.collidepoint((mx, my)):
            if click:
                main_menu()

        pg.display.update()
        clock.tick(60)

# -------- Main Program Loop ----------- #
def game():

    levels()

    score = 0
    round = 1

    mx, my = pg.mouse.get_pos()

    done = False
    #click = False
    while not done:
        # --- Main event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    player.left_pressed = True
                if event.key == pg.K_d:
                    player.right_pressed = True
                if event.key == pg.K_w:
                    player.up_pressed = True
                if event.key == pg.K_s:
                    player.down_pressed = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_a:
                    player.left_pressed = False
                if event.key == pg.K_d:
                    player.right_pressed = False
                if event.key == pg.K_w:
                    player.up_pressed = False
                if event.key == pg.K_s:
                    player.down_pressed = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1 and player.up_pressed == True:
                    player_sword = Sword(player.rect.x+5, player.rect.y-80, BLUE, 10, 50)
                    sword_group.add(player_sword)
                    sword_hit_group = pg.sprite.spritecollide(player_sword, enemy_group, True)
                    for my_enemy in sword_hit_group:
                        enemy_group.remove(my_enemy)
                        all_sprites_group.remove(my_enemy)
                        score += 100
                if event.button == 1 and player.down_pressed == True:
                    player_sword = Sword(player.rect.x+5, player.rect.y+60, BLUE, 10, 40)
                    sword_group.add(player_sword)
                    sword_hit_group = pg.sprite.spritecollide(player_sword, enemy_group, True)
                    for my_enemy in sword_hit_group:
                        enemy_group.remove(my_enemy)
                        all_sprites_group.remove(my_enemy)
                        score += 100
                if event.button == 1 and player.left_pressed == True:
                    player_sword = Sword(player.rect.x-60, player.rect.y+5, BLUE, 50, 10)
                    sword_group.add(player_sword)
                    sword_hit_group = pg.sprite.spritecollide(player_sword, enemy_group, True)
                    for my_enemy in sword_hit_group:
                        enemy_group.remove(my_enemy)
                        all_sprites_group.remove(my_enemy)
                        score += 100
                if event.button == 1 and player.right_pressed == True:
                    player_sword = Sword(player.rect.x+60, player.rect.y+5, BLUE, 50, 10)
                    sword_group.add(player_sword)
                    sword_hit_group = pg.sprite.spritecollide(player_sword, enemy_group, True)
                    for my_enemy in sword_hit_group:
                        enemy_group.remove(my_enemy)
                        all_sprites_group.remove(my_enemy)
                        score += 100
                if event.button == 3 and player.up_pressed == True:
                    player_shield = Sword(player.rect.x-5, player.rect.y-12, CYAN, 30, 10)
                    sword_group.add(player_shield)
                if event.button == 3 and player.down_pressed == True:
                    player_shield = Sword(player.rect.x-5, player.rect.y-32, CYAN, 30, 10)
                    sword_group.add(player_shield)
                if event.button == 3 and player.right_pressed == True:
                    player_shield = Sword(player.rect.x-12, player.rect.y-5, CYAN, 10, 30)
                    sword_group.add(player_shield)
                if event.button == 3 and player.left_pressed == True:
                    player_shield = Sword(player.rect.x-32, player.rect.y-5, CYAN, 10, 30)
                    sword_group.add(player_shield)
            if event.type == pg.MOUSEBUTTONUP:
                sword_group.empty()


        # --- Game logic should go here
        #if click:
            #player_sword = Sword(100, 100, BLUE, 10, 30)
            #all_sprites_group.add(player_sword)
            #for x in range(1, 801):
                #player_sword.counter += 1

            #player_sword.time = pg.time.get_ticks()

        ## -- COLLISION DETECTION OF PLAYER AND WALL SPRITES -- ##
        player_collision = pg.sprite.spritecollide(player, wall_group, False)
        for i in player_collision:
            player.rect.x = old_player_x
            player.rect.y = old_player_y
        #next i

        old_player_x = player.rect.x
        old_player_y = player.rect.y

        if not enemy_group:
            wall_group.empty()
            draw_map(map2)
            if player.rect.y < 0:
                round += 1
                player.rect.y = 650
                levels()

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BLACK)
        all_sprites_group.draw(screen)
        wall_group.draw(screen)
        sword_group.draw(screen)
        sword_group.update()
        enemy_group.update()
        all_sprites_group.update()
        # --- Drawing code should go here
        # - Text on screen
        draw_text(f"Score: {score}", font3, WHITE, screen, 1300, 10)
        draw_text(f"Round: {round}", font3, WHITE, screen, 1300, 35)

        # --- Go ahead and update the screen with what we've drawn.
        pg.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

main_menu()

pg.quit()
