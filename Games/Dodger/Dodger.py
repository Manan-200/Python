import pygame
import random
import os
import time

pygame.font.init()
pygame.mixer.init()

time_survived = 0
w, h = 1000, 700
player_w, player_h = 50, 50
running, lost, start_state = True, False, False
player_vel, meteor_vel = 3, 6
fps = 120
clock = pygame.time.Clock()
meteor_list = [] 
bg_y = 0

death_msg_font = pygame.font.SysFont("comicsans", 100)
time_font = pygame.font.SysFont("comicsans", 50)
main_menu_font = pygame.font.SysFont("comicsans", 60)
ctrl_font = pygame.font.SysFont("comicsans", 40)

collision_sound = pygame.mixer.Sound(os.path.join("assets", "sound_effect.wav"))

win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Dodger")

player_img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "spaceship_red.png")), (player_w, player_h)), 180)
bg_img1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space_img.png")), (w, h))
bg_img2 = bg_img1
meteor_img = pygame.image.load(os.path.join("assets", "meteor_img3.png")).convert_alpha()
meteor_img.set_colorkey((255, 255, 255))

class Meteor:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.mask = pygame.mask.from_surface(meteor_img)
        
    def move(self, vel):
        self.y += vel
    
    def draw(self, window):
        window.blit(meteor_img, (self.x, self.y))

    def check_off_screen(self):
        if self.y > h:
            meteor_list.remove(meteor)

class Player:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.player_img = player_img
        self.mask = pygame.mask.from_surface(self.player_img)

    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))

    def draw_health(self):
        health_barRect = pygame.Rect(self.x, self.y + player_h + 2, player_w, 6)
        health_amtRect = pygame.Rect(self.x, self.y + player_h + 2, player_w * self.health/100, 6)
        pygame.draw.rect(win, (255, 0, 0), health_barRect)
        pygame.draw.rect(win, (0, 255, 0), health_amtRect)

def handle_collisions(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    if obj1.mask.overlap(obj2.mask, (offset_x, offset_y)):
        player.health -= 5
        collision_sound.play()
        meteor_list.remove(meteor) 

def reset():
    player.health = 100
    meteor_list.clear()
    player.x = w/2
    player.y = h - player_h - 10

player = Player(w / 2, h - player_h - 10)



while running:

    clock.tick(fps)

    time_text = time_font.render(f"Score : {round(time_survived/fps)}", 1, (255, 255, 255))
    menu_text = main_menu_font.render("Click to start", 1, (255, 255, 255))
    death_msg = death_msg_font.render("You Ded!", 1, (255, 255, 255))
    ctrl_text = ctrl_font.render("Controls : W, A, S, D", 1, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_state = True

    if start_state == False:
        reset()
        time_survived = 0
        win.blit(bg_img1, (0, 0))
        win.blit(menu_text, ((w//2 - menu_text.get_width()/2), (h//2 - menu_text.get_height()/2)))
        win.blit(ctrl_text, ((w//2 - ctrl_text.get_width()/2), (h//2 - ctrl_text.get_height()/2 + menu_text.get_height())))
        pygame.display.update()

    elif start_state == True:

        time_survived += 1
        
        if bg_y >= 0 and bg_y <= h:
            win.blit(bg_img2, (0, bg_y - h))
        if bg_y > h:
            bg_y = 0
        win.blit(bg_img1, (0, bg_y))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_w < w:
            player.x += player_vel
        if keys[pygame.K_w] and player.y > 0:
            bg_y += 1
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_h < h:
            bg_y -= 0.5
            player.y += player_vel

        player.draw(win)
        player.draw_health()

        if len(meteor_list) < 20:
            meteor = Meteor(random.randrange(0, w - 10), random.randrange(-800, - 10), 50, 50)
            meteor_list.append(meteor)

        for meteor in meteor_list[:]:
            meteor.move(meteor_vel)
            meteor.draw(win)
            meteor.check_off_screen()
            handle_collisions(player, meteor)

        if player.health <= 0:
            lost = True

        elif player.health > 0:
            lost = False

        if lost:
            win.blit(death_msg, (w//2 - death_msg.get_width()//2, h//2 - death_msg.get_height()//2))
            win.blit(time_text, (w//2 - time_text.get_width()//2, h//2 - time_text.get_height()//2 + death_msg.get_height()))
            pygame.display.update()
            time.sleep(3)
            start_state = False

        amplifier = 0.2 * time_survived/fps

        if amplifier > 10:
            amplifier = 10

        bg_y += amplifier
        
        pygame.display.update()