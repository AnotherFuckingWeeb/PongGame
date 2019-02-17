import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Goals/goal1.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 690
    
    def Draw(self, screen):
        screen.blit(self.image, self.rect)

class Goal2(Goal):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Goals/goal2.png")
        self.rect.centery = 90