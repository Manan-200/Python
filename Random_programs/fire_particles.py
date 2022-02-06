import pygame
import random

w, h = 1000, 700
fps = 120
particle_list, meteorlist = [], []
particle_state = True
particle_x, particle_y = 0, 0
max_time = 0.1
rate = 0
meteor_vel = 5

win = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

class Particles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.time = 0
        self.color = None

    def draw(self):
        if self.time < max_time/2 * fps + 4:
            self.color = (255, 0, 0)
        if self.time > max_time/2 * fps + 4:
            #self.color = (132, 136, 132)
            self.color = (226, 88, 34)
        self.time += 1
        particle_h = random.randrange(2, 8)
        particle_w = particle_h
        pygame.draw.rect(win, self.color, (self.x, self.y, particle_w, particle_h))

class Meteor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.Rect = pygame.Rect(self.x, self.y, 25, 25)
        pygame.draw.rect(win, (0, 0, 255), self.Rect)

    def move(self, vel):
        self.y += vel

while True:

    clock.tick(fps)

    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    while len(meteorlist) < 1:
        player = Meteor(random.randrange(10, w - 25), 0)
        meteorlist.append(player)

    for player in meteorlist:
        player.draw()
        player.move(meteor_vel)
        if player.y > h:
            player.y = 0
            meteorlist.remove(player)

        while len(particle_list) < 20:
            rate -= 4
            particle = Particles(random.randrange((player.x), (player.x + 25)) , player.y + rate + player.Rect[3] - 5)
            particle_list.append(particle)
        rate = 0

    for particle in particle_list[:]:
        particle.draw()
        if particle.time > max_time * fps:
            particle_list.remove(particle)
            particle_state = False
        if particle_state == False:
            particle.time = 0
            particle_state = True

    pygame.display.update()