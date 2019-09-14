import pygame
from settings import *
import random
from os import path

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        pygame.draw.ellipse(self.image, RED, (0, 0, 20, 20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.rect.x = DISPLAY_WIDTH / 2
        self.rect.y  = DISPLAY_HEIGHT / 2
        
        self.speed_x = 0
        self.speed_y = 0
        
        self.radius = 20

    def update(self):
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        elif keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        else:
            self.speed_x = 0
        
        if keystate[pygame.K_DOWN]:
            self.speed_y = 5
        elif keystate[pygame.K_UP]:
            self.speed_y = -5
        else:  
            self.speed_y = 0
                      
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        self.rect.height = self.radius
        self.rect.width = self.radius
        self.image = pygame.Surface((self.radius, self.radius))
        pygame.draw.ellipse(self.image, RED, (0, 0, 20, 20))
        self.image.set_colorkey(BLACK)
        
        if self.rect.right > DISPLAY_WIDTH:
            self.rect.right = DISPLAY_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > DISPLAY_HEIGHT:
            self.rect.bottom = DISPLAY_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
         
    def grow(self):
        self.radius += int(80 / self.radius)
    


class Point(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.point_x = random.randint(0,1200)
        self.point_y = random.randint(0,600)
        
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)

        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = self.point_x
        self.rect.y = self.point_y