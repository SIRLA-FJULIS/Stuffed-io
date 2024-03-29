import pygame
from sprites import *
from settings import *
from os import path
import random
import time
        
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.font_filename = pygame.font.match_font('arial') # 字型
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True 
        
        self.all_sprites = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        for i in range(30):
            p = Point()
            self.all_sprites.add(p)
            self.points.add(p)
        
    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font(self.font_filename, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)
        
    def new(self):
        self.playing = True
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitgame(self)
                
    def collision_check(object_A, object_B):#碰撞檢查
        return(pygame.sprite.collide_circle(object_A,object_B)) #判斷兩個rect是否有碰撞
                
    def update(self):
        self.all_sprites.update()
        for i in self.points:
            if pygame.sprite.collide_circle(self.player, i):
                self.all_sprites.remove(i)
                self.points.remove(i)
                self.player.grow()
                
        if len(self.points) < 30:
            p = Point()
            self.all_sprites.add(p)
            self.points.add(p)
            
    def draw(self):
        self.screen.fill(WHITE) #背景底色
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
        
    def run(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def game_intro(self):
        pass
    def gameover(self):
        pass
        
    def quitgame():
        quit()

game = Game()

while game.running:
    game.new()
    game.run()
    game.over()