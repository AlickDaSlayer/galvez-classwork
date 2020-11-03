### SRC - This is a good start, but I'd like to see something
### a bit more playable!

import pygame
import random
import math

# -- Coulour Constants -- #

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
pygame.font.init()

# -- Initialise the screen -- #

DIMENSIONS = (640, 480)
SCREEN = pygame.display.set_mode(DIMENSIONS)

pygame.display.set_caption("Space Invaders")

class Invaders(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the invader
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-50, -10)
        self.speed = 1

    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y == 480:
            self.rect.x = random.randrange(0, 600)
            self.rect.y = random.randrange(-50, -10)
            player.lives -= 1
    #end procedure
#end class

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the player
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 450
        self.speed = 0
        self.lives = 5
        self.bullet_count = 50
        
    def player_set_speed(self, val):
        self.speed =+ val
        if(self.rect.x < 0):
            self.rect.x = 0
        elif(self.rect.x > 630):
            self.rect.x = 630

    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.y == 480:
            self.rect.x = 300
            self.rect.y = 450

class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 4

    def update(self):
        self.rect.y = self.rect.y - self.speed

done = False    # - Control variable

font = pygame.font.SysFont('Calibri', 25, True, False)
big_font = pygame.font.SysFont('Calibri', 50, True, False)

score = 0

invader_group = pygame.sprite.Group()   # - Create a list of the invader blocks
bullet_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()   # - Create a list of all sprites

number_of_invaders = 10
for x in range(number_of_invaders):
    my_invader = Invaders(BLUE, 20, 20, 1)
    invader_group.add(my_invader)
    all_sprites_group.add(my_invader)

player = Player(YELLOW, 20, 20)
all_sprites_group.add(player)

clock = pygame.time.Clock() # - Creates a pygame clock to regulate fps in game

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bullet = Bullet(GREEN, 4, 8, player.rect.x + 8, player.rect.y)
                bullet_group.add(bullet)
                all_sprites_group.add(bullet)
                player.bullet_count = player.bullet_count - 1

    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_LEFT]:
            player.player_set_speed(-7)
        if keys[pygame.K_RIGHT]:
            player.player_set_speed(7)
    elif event.type == pygame.KEYUP:
        player.player_set_speed(0)

    # -- Game logic goes after this comment

    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    for x in player_hit_group:
        player.lives = player.lives - 1

    for bullet in bullet_group:
        bullet_hit_group = pygame.sprite.spritecollide(bullet, invader_group, True)
        for my_invader in bullet_hit_group:
            bullet_group.remove(bullet)
            all_sprites_group.remove(bullet)
            score += 100
        if bullet.rect.y < -10:
            bullet_group.remove(bullet)
            all_sprites_group.remove(bullet)

    all_sprites_group.update()

    SCREEN.fill(BLACK)

    all_sprites_group.draw(SCREEN)

    # - Text on screen
    label_score = font.render(f"Score: {score}", True, WHITE)
    SCREEN.blit(label_score, [10, 10])
    label_lives = font.render(f"Lives: {player.lives}", True, WHITE)
    SCREEN.blit(label_lives, [10, 40])

    if player.lives == 0:
        all_sprites_group.empty()
        over_text = big_font.render("Game Over...", True, WHITE)
        over_rect = over_text.get_rect()
        over_x = SCREEN.get_width() / 2 - over_rect.width / 2
        over_y = SCREEN.get_height() / 2 - over_rect.height / 2
        SCREEN.blit(over_text, [over_x, over_y])

    # -- Flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
