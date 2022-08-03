import pygame
import random
import math

width, height = 1500, 700
win = pygame.display.set_mode((width, height))
fps = 120
clock = pygame.time.Clock()
G = 6.67 * 10 ** -11
planet_list = []
planets = 50

def get_dist(x1, y1, x2, y2):
    a = x1 - x2
    b = y1 - y2
    return (a ** 2 + b ** 2) ** 0.5

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.x_vel = 0
        self.y_vel = 0
        self.ax = 0
        self.ay = 0
    def draw(self):
        pygame.draw.circle(win, (255, 255, 255), (int(self.x), int(self.y)), 3)
    def move(self):
        self.x_vel += self.ax/fps
        self.y_vel += self.ay/fps
        self.x += self.x_vel/fps
        self.y += self.y_vel/fps

for i in range(planets):
    planet_list.append(Planet(random.randint(0, width), random.randint(0, height), 10**12))

run = True
while run:

    clock.tick(fps)

    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(len(planet_list)):
        for j in range(i, len(planet_list)):
            p1 = planet_list[i]
            p2 = planet_list[j]
            if p2 != p1:
                #Calculations
                R = get_dist(p1.x, p1.y, p2.x, p2.y)
                F = G * p1.mass * p2.mass / (R ** 2)
                theta = math.asin(abs(p1.x - p2.x)/R)
                
                Fx = F * math.cos(theta)
                Fy = F * math.sin(theta)
                
                #Defining accelerations
                p1.ax =  Fx/p1.mass
                p1.ay = Fy/p1.mass
                p2.ax = Fx/p2.mass
                p2.ay = Fy/p2.mass

                if p1.x > p2.x:
                    p1.ax *= -1
                else:
                    p2.ax *= -1
                if p1.y > p2.y:
                    p1.ay *= -1
                else:
                    p2.ay *= -1

                #Moving planets
                p1.move()
                p2.move()
    
    for planets in planet_list:
        planets.draw()

    pygame.display.update()