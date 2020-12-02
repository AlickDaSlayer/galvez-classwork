import pygame
import sys
from maps import map1, map2

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
pg = pygame

# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pg.display.set_mode(size)

font1 = pg.font.SysFont(None, 200)
font2 = pg.font.SysFont(None, 100)

pg.display.set_caption("My Game")

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
        self.speed = 1

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

class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, colour, w, h):
        super().__init__()
        self.image = pg.Surface([w,h])
        self.image.fill(colour)
        # Set the position of the player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Sword(pg.sprite.Sprite):
    def __init__(self, x, y, colour, w, h):
        super().__init__()
        self.image = pg.Surface([w,h])
        self.image.fill(colour)
        # Set the position of the player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


all_sprites_group = pg.sprite.Group()

player = Player(500, 400, GREEN, 20, 20)
all_sprites_group.add(player)

wall_group = pg.sprite.Group()

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

draw_map(map1)

# Used to manage how fast the screen updates
clock = pg.time.Clock()

def draw_text(text, font, colour, suface, x, y):
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
                pass


        pg.display.update()
        clock.tick(60)


# -------- Main Program Loop ----------- #
def game():
    done = False
    click = False
    counter = 0
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
                if event.button == 1:
                    player_sword = Sword(player.rect.x+5, player.rect.y-30, BLUE, 10, 30)
                    all_sprites_group.add(player_sword)
                
                    all_sprites_group.remove(player_sword)



        # --- Game logic should go here

        ## -- COLLISION DETECTION OF PLAYER AND WALL SPRITES -- ##
        player_collision = pg.sprite.spritecollide(player, wall_group, False)
        for i in player_collision:
            player.rect.x = old_player_x
            player.rect.y = old_player_y
        #next i

        old_player_x = player.rect.x
        old_player_y = player.rect.y

        if player.rect.y < 0:
            player.rect.y = 700
            wall_group.empty()
            draw_map(map2)
        #endif
        if player.rect.y > 720:
            player.rect.y = 20
            wall_group.empty()
            draw_map(map1)
        #endif

        # --- Screen-clearing code goes here
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BLACK)
        all_sprites_group.draw(screen)
        wall_group.draw(screen)
        all_sprites_group.update()
        # --- Drawing code should go here

        # --- Go ahead and update the screen with what we've drawn.
        pg.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(400)


main_menu()

pg.quit()
