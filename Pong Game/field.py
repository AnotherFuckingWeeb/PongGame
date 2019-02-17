import pygame


def Field(screen, color):
    #Field
    pygame.draw.rect(screen, color, [50, 90, 700, 600], 2)
    #Line 1
    pygame.draw.line(screen, color, [50, 375], [388, 375], 2)
    #Line 2
    pygame.draw.line(screen, color, [413, 375], [750, 375], 2)
    #Circle
    pygame.draw.circle(screen, color, [400, 375], 12, 1)

    