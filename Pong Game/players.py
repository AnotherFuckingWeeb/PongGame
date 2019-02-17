import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Players/player1.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 120
        self.rect.centery = 650
        self.vel = 10

    def Draw(self, screen):
        screen.blit(self.image, self.rect)

class Player2(Player):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Players/player2.png")
        self.rect.centerx = 180
        self.rect.centery = 130