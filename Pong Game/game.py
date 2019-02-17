import pygame
import random
from players import *
from ball import *
from field import *
from goals import *

WIDTH = 800
HEIGHT = 800
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
player = Player()
player2 = Player2()
ball = Ball()
goal = Goal()
goal2 = Goal2()
score = 0
score2 = 0
font = pygame.font.SysFont("comicsans", 90)
hit_player = pygame.mixer.Sound("Sounds/player.ogg")
point = pygame.mixer.Sound("Sounds/point.ogg")



def ScoreBoard(screen, score, score2):
    score = font.render(str(score), True, (255, 255, 255))
    score2 = font.render(str(score2), True, (255, 255, 255))
    bar = font.render("-", True, (255, 255, 255))
    screen.blit(score, [315, 30])
    screen.blit(score2, [450, 30])
    screen.blit(bar, [390, 25])

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.rect.centerx > 107:
        player.rect.centerx -= player.vel
    
    if keys[pygame.K_RIGHT] and player.rect.centerx < 695:
        player.rect.centerx += player.vel
    if keys[pygame.K_RETURN]:
        ball.start = True

    if player2.rect.centerx < 695:
        player2.rect.centerx = ball.rect.centerx
    if player2.rect.centerx > 107:
        player2.rect.centerx = ball.rect.centerx

    if ball.rect.colliderect(player.rect) or ball.rect.colliderect(player2.rect):
        ball.speed[1] = -ball.speed[1]
        hit_player.play()
    if ball.rect.colliderect(goal.rect):
        score += 1
        point.play()
        ball.start = False
        ball.rect.centerx = 400
        ball.rect.centery = 375
    if ball.rect.colliderect(goal2.rect):
        score2 += 1
        point.play()
        ball.start = False
        ball.rect.centerx = 400
        ball.rect.centery = 375


    # Draw / render
    screen.fill(BLACK)
    ScoreBoard(screen, score, score2)
    Field(screen, WHITE)
    player.Draw(screen)
    player2.Draw(screen)
    ball.Draw(screen)
    goal.Draw(screen)
    goal2.Draw(screen)
    print(score)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()