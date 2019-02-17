import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Ball/ball.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 375
        self.speed = [10,10]
        self.sound = pygame.mixer.Sound("Sounds/wall.ogg")
        self.start_sound = pygame.mixer.Sound("Sounds/start.ogg")
        self.start = False
    
    def Draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.start:
            self.start_sound.play(0, 1, 0)
            if self.rect.left < 50 or self.rect.right > 750:
                self.sound.play()
                self.speed[0] = -self.speed[0]
            if self.rect.top < 90 or self.rect.bottom > 690:
                self.sound.play()
                self.speed[1] = -self.speed[1]
            self.rect.move_ip(self.speed[0], self.speed[1])
    
        