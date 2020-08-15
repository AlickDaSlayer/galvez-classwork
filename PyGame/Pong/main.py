import pygame
from game import Paddle
from game import Ball

pygame.init()

win = pygame.display.set_mode((750, 500))

pygame.display.set_caption('PONG')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715
paddle2.rect.y = 225

pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, pong)
clock = pygame.time.Clock()

def redraw():
    win.fill(BLACK)
    # -- Title Font
    font = pygame.font.SysFont('Halvetica', 30)
    text = font.render('PONG', False, WHITE)
    textRect = text.get_rect()
    textRect.center = (750//2, 25)
    win.blit(text, textRect)

    # -- Player One Score
    p1_score = font.render(str(paddle1.points), False, WHITE)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    win.blit(p1_score, p1Rect)

    # -- Player Two Score
    p2_score = font.render(str(paddle2.points), False, WHITE)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    win.blit(p2_score, p2Rect)

    all_sprites.draw(win)
    pygame.display.update()
    clock = pygame.time.Clock()

run = True

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y += -paddle1.speed
    if key[pygame.K_s]:
        paddle1.rect.y += paddle1.speed
    if key[pygame.K_UP]:
        paddle2.rect.y += -paddle2.speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += paddle2.speed

    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    # -- Ball Collisions
    if pong.rect.y > 490:
        pong.dy = -1
    if pong.rect.x > 740:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = -1
        paddle1.points += 1
    if pong.rect.y < 10:
        pong.dy = 1
    if pong.rect.x < 10:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = 1
        paddle2.points += 1
    if paddle1.rect.colliderect(pong.rect):
        pong.dx = 1
    if paddle2.rect.colliderect(pong.rect):
        pong.dx = -1

    # -- Paddle Boundaries
    if paddle1.rect.y < 0:
        paddle1.rect.y = 0
    if paddle1.rect.y > 425:
        paddle1.rect.y = 425
    if paddle2.rect.y < 0:
        paddle2.rect.y = 0
    if paddle2.rect.y > 425:
        paddle2.rect.y = 425

    redraw()
pygame.quit()


