import pygame
import os
import random

width, height = 1000, 600
player_vel = 10
bg_x, bg_y = -500, -500
fps = 60
rock_list = []
clock = pygame.time.Clock()

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Indie Game")

bg_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img.png")), (width + 2*(-bg_x), height + 2*(-bg_y)))

class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw(self):
        self.Rect = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        pygame.draw.rect(win, (255, 0, 0), self.Rect)

class Rock:
    def __init__(self):
        self.x = random.randrange(1, bg_img.get_width())
        self.y = random.randrange(1, bg_img.get_height())
    def draw(self):
        self.Rect = pygame.Rect(bg_x + self.x, bg_y + self.y, 10, 10)
        pygame.draw.rect(win, (128, 132, 135), self.Rect)

player = Player(width/2, height/2, 10, 10)

running = True
while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.x - player.h > bg_x:
        bg_x += player_vel
    if keys[pygame.K_d] and player.x + player.h < bg_x + bg_img.get_width():
        bg_x -= player_vel
    if keys[pygame.K_w] and player.y - player.h > bg_y:
        bg_y += player_vel
    if keys[pygame.K_s] and player.y + player.h < bg_y + bg_img.get_height():
        bg_y -= player_vel

    while len(rock_list) < 100:
        rock = Rock()
        rock_list.append(rock)

    win.blit(bg_img, (bg_x, bg_y))
    player.draw()
    for rock in rock_list:
        rock.draw()
    
    pygame.display.update()