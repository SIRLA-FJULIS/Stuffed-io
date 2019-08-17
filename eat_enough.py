import pygame
import time
import random

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

width = 1200
height = 600
fps = 30

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("吃粗飽.io")
clock = pygame.time.Clock()

speed_x = 0
speed_y = 0

radius = 20
running = True
points = []

class Player():
	def __init__(self, screen, speed_x, speed_y, radius):
		self.screen = screen
		self.player_x = 400
		self.player_y = 250
		
	def update(self):
		self.surf = pygame.Surface((radius, radius))
		self.rect = self.surf.get_rect()
        
		self.player_x += speed_x
		self.player_y += speed_y
		self.rect.x = self.player_x
		self.rect.y = self.player_y
	def draw(self):
		pygame.draw.ellipse(screen, black, (self.player_x, self.player_y, radius, radius))
"""
以下為直接跟著滑鼠移動版本
    def update(self):
        self.surf = pygame.Surface((radius, radius))
        self.rect = self.surf.get_rect()
        
        self.pos = pygame.mouse.get_pos()
        
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
    def draw(self):
        pygame.draw.ellipse(screen, black, (self.pos[0], self.pos[1], radius, radius))

"""
class Point():
	def __init__(self, screen):
		self.screen = screen
		self.point_x = random.randint(0,1200)
		self.point_y = random.randint(0,600)
		self.r = random.randint(0,255)
		self.g = random.randint(0,255)
		self.b = random.randint(0,255)

		self.surf = pygame.Surface((10, 10))
		self.rect = self.surf.get_rect()
		self.rect.centerx = self.point_x
		self.rect.centery = self.point_y

	def draw(self):
		pygame.draw.ellipse(screen, (self.r, self.g, self.b), (self.point_x, self.point_y, 10, 10))

def collision_check(object_A, object_B):
    #碰撞檢查
    return(object_A.rect.colliderect(object_B.rect)) #判斷兩個rect是否有碰撞

def screen_update():
	global radius
	screen.fill(white)
	
	for i in points:
		i.draw()
		if collision_check(player, i):
			points.remove(i)
			radius += 80 / radius

		

	player.draw()

	pygame.display.flip()

player = Player(screen, speed_x, speed_y, radius)
point = Point(screen)

def gameloop():
	global speed_x, speed_y, r, g, b, h, w
	clock.tick(fps)
	screen.fill(white) #背景底色
	
	player.update()
	screen_update()
	
	#判斷按鍵有沒有按下
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				speed_x = -7
			elif event.key == pygame.K_RIGHT:
				speed_x = 7

			if event.key == pygame.K_UP:
				speed_y = -7
			elif event.key == pygame.K_DOWN:
				speed_y = 7

		elif event.type == pygame.KEYUP:
			speed_x = 0
			speed_y = 0

	if len(points) < 20:
		points.append(Point(screen))

	


def pygamequit():
	quit()

while running:
	gameloop()
