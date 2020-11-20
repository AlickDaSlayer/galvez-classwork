import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
pg = pygame
 
# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pg.display.set_mode(size)
 
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
        self.speed = 0

    def movePlayer(self,x,y):
        self.rect.x += x
        self.rect.y += y 

class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pg.Surface([w,h])
        self.image.fill(RED)
        # Set the position of the player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       ]

        
all_sprites_group = pg.sprite.Group()

player = Player(500, 400, GREEN, 20, 20)
all_sprites_group.add(player)

wall_group = pg.sprite.Group()

x = 0
y = 0

for row in map:
    for col in row:
        if col == 1:
            my_wall = Wall(x, y, 40, 40)
            wall_group.add(my_wall)
            all_sprites_group.add(my_wall)
        x += 40
    x = 0
    y += 40

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pg.time.Clock()
 
# -------- Main Program Loop ----------- #
while not done:
    # --- Main event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    keys = pg.key.get_pressed()

    if event.type == pg.KEYDOWN:
        if keys[pg.K_LEFT]:
            player.movePlayer(-1,0)
        if keys[pg.K_RIGHT]:
            player.movePlayer(1,0)
        if keys[pg.K_UP]:
            player.movePlayer(0,-1)
        if keys[pg.K_DOWN]:
            player.movePlayer(0,1)
    elif event.type == pg.KEYUP:
        player.movePlayer(0,0)

    
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    all_sprites_group.draw(screen)

    all_sprites_group.update()
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(1000)
 
# Close the window and quit.
pg.quit()
