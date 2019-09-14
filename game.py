import pygame
from network import Network
from random import randint
from settings import *
import os

class Player():
    def __init__(self, screen, startx, starty, color, score, name):
        self.screen = screen
        self.pos_x = startx
        self.pos_y = starty
        self.color = color
        self.score = score
        self.name = name
        self.radius = 20
        
    def update(self):
        self.surf = pygame.Surface((self.radius, self.radius))
        self.rect = self.surf.get_rect()        
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.rect = self.surf.get_rect()
        
    def draw(self):
        pygame.draw.ellipse(self.screen, self.color, (self.pos_x, self.pos_y, self.radius, self.radius))
            
class Game:
    
    def __init__(self, w, h, name):
        self.net = Network()
        self.id = self.net.connect(name)
        print(self.id)
        
        self.width = w
        self.height = h
        self.canvas = Canvas(self.width, self.height, TITLE)
        
        self.players = []
        players_data = self.net.send("get_players")
        for id, player_data in players_data.items():
            print(player_data)
            self.players.append(Player(self.canvas.get_canvas(), player_data["x"], player_data["y"], \
                                player_data["color"], player_data["score"], player_data["name"]))
        
    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                if event.type == pygame.K_ESCAPE:
                    run = False
            
            # key events
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if self.players[self.id].pos_x + self.players[self.id].radius <= DISPLAY_WIDTH:
                    self.net.send("move {} right".format(self.id))
                    
            if keys[pygame.K_LEFT]:
                if self.players[self.id].pos_x >= 0:
                    self.net.send("move {} left".format(self.id))
                    
            if keys[pygame.K_UP]:
                if self.players[self.id].pos_y >= 0:
                    self.net.send("move {} up".format(self.id))
                    
            if keys[pygame.K_DOWN]:
                if self.players[self.id].pos_y + self.players[self.id].radius <= DISPLAY_HEIGHT:
                    self.net.send("move {} down".format(self.id))
            
            # update all
            players_data = self.net.send("get_players")
            current_id = len(players_data) - 1
            if len(players_data) > len(self.players):
                self.players.append(Player(self.canvas.get_canvas(), players_data[current_id]["x"], players_data[current_id]["y"], \
                                    players_data[current_id]["color"], players_data[current_id]["score"], players_data[current_id]["name"]))
            
            for id, player_data in players_data.items():
                self.players[id].pos_x = players_data[id]["x"]
                self.players[id].pos_y = players_data[id]["y"]
                self.players[id].score = players_data[id]["score"]
                self.players[id].update()
            
            # Update Canvas
            self.canvas.draw_background()
            for player in self.players:
                player.draw()
            self.canvas.update()
                
            clock.tick(60)
            
        pygame.quit()
        
class Canvas:
    
    def __init__(self, w, h, name="None"):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        
    @staticmethod
    def update():
        pygame.display.update()
     
    def draw_text(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", size)
        render = font.render(text, 1, (0, 0, 0))
        
        self.screen.draw(render, (x, y))
        
    def get_canvas(self):
        return self.screen
    
    def draw_background(self):
        self.screen.fill((255, 255, 255))
        
if __name__ == "__main__":
    while True:
        name = input("Please enter your name: ")
        if  0 < len(name) < 20:
            break
        else:
            print("Error, this name is not allowed (must be between 1 and 19 characters [inclusive])")
            
    # make window start in top left hand corner
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)
    
    g = Game(DISPLAY_WIDTH, DISPLAY_HEIGHT, name)
    g.run()