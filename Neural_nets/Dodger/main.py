import pygame
import random
import os
import neat

pygame.font.init()
pygame.mixer.init()

w, h = 1000, 700
ship_w, ship_h = 50, 50
ship_vel, meteor_vel = 3, 6
fps = 120
clock = pygame.time.Clock()

collision_sound = pygame.mixer.Sound(os.path.join("assets", "sound_effect.wav"))

win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Dodger")

ship_img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "spaceship_red.png")), (ship_w, ship_h)), 180)
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
        self.Rect = pygame.Rect(self.x, self.y, self.w, self.h)
        window.blit(meteor_img, (self.x, self.y))

    def check_off_screen(self, meteor_list):
        if self.y > h:
            meteor_list.remove(self)

class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = ship_img
        self.mask = pygame.mask.from_surface(self.ship_img)

    def draw(self, window):
        self.Rect = pygame.Rect(self.x, self.y, self.ship_img.get_width(), self.ship_img.get_height())
        window.blit(self.ship_img, (self.x, self.y))

    def draw_health(self):
        health_barRect = pygame.Rect(self.x, self.y + ship_h + 2, ship_w, 6)
        health_amtRect = pygame.Rect(self.x, self.y + ship_h + 2, ship_w * self.health/100, 6)
        pygame.draw.rect(win, (255, 0, 0), health_barRect)
        pygame.draw.rect(win, (0, 255, 0), health_amtRect)

def collided(obj1, obj2, meteor_list, ship_list):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    if obj1.mask.overlap(obj2.mask, (offset_x, offset_y)):
        return(True)

def main(genomes, config):
    nets = []
    ge = []
    ships = []

    for i, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        ships.append(Ship((i + 1) * 10, h - ship_h - 10))
        g.fitness = 0
        ge.append(g)

    score = 0

    bg_y = 0
    time_survived = 0
    meteor_list = []
    meteors_100 = []

    running = True
    while running:

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        if True:

            time_survived += 1
            
            if bg_y >= 0 and bg_y <= h:
                win.blit(bg_img2, (0, bg_y - h))
            if bg_y > h:
                bg_y = 0
            win.blit(bg_img1, (0, bg_y))

            for ship in ships:
                ship.draw(win)
                ship.draw_health()

            if len(meteor_list) < 20:
                meteor = Meteor(random.randrange(0, w - 10), random.randrange(-800, - 10), 50, 50)
                meteor_list.append(meteor)

            for meteor in meteor_list:

                meteor.move(meteor_vel)
                meteor.draw(win)
                meteor.check_off_screen(meteor_list)

                for ship in ships:
                    if collided(ship, meteor, meteor_list, ships):
                        collision_sound.play()
                        if ship in ships:
                            ships.remove(ship)
                        if meteor in meteor_list:
                            meteor_list.remove(meteor)

                if abs(ship.y - meteor.y) <= 100 and abs(ship.x - meteor.x) <= 100 and meteor not in meteors_100:
                    meteors_100.append(meteor)
                if abs(ship.y - meteor.y) >  100 and abs(ship.x - meteor.x) > 100 and meteor in meteors_100:
                    meteors_100.remove(meteor)

            

            amplifier = 0.2 * time_survived/fps

            if amplifier > 10:
                amplifier = 10

            bg_y += amplifier
            
            pygame.display.update()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation,
                            config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path)