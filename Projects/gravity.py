import pygame
import math
import random

pygame.font.init()

pi = 22/7
planets= 10000
planet_list = []
p_xy = []
pos_count = 0
p_mass = 100
s_mass = 54*(10**15)
width, height = 1500, 700
G = 6.67 * (10 ** (-11))
fps = 120
selected = False
clock = pygame.time.Clock()

win = pygame.display.set_mode((width, height))
stats_font = pygame.font.SysFont("calibri", 20)
planets_font = pygame.font.SysFont("calibri", 30)

def get_dist(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    return((a**2 + b**2)**(1/2))

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.w = 3
        self.h = 3
        self.mass = mass
        self.x_vel = random.choice([50, -50])
        self.y_vel = random.choice([50, -50])
    def draw(self):
        self.Rect = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        pygame.draw.rect(win, (0, 0, 255), self.Rect)

class Star:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.w = 15
        self.h = 15
        self.mass = mass
    def draw(self):
        self.Rect = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        pygame.draw.rect(win, (255, 0, 0), self.Rect)

star = Star(int(width/2), int(height/2), s_mass)
for i in range(planets):
    planet = Planet(random.randrange(star.x - 150, star.x + 150), random.randrange(star.y - 150, star.y + 150), p_mass)
    planet_list.append(planet)


run = True
while run:

    clock.tick(fps)

    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_pos = pygame.mouse.get_pos()
    for planet in planet_list:
        #Calculations
        R = get_dist(planet.x, planet.y, star.x, star.y)
        theta = math.asin((abs(planet.y - star.y))/R)
        F = (planet.mass * star.mass * G)/(R**2)
        Fx = F*math.cos(theta)
        Fy = F*math.sin(theta)
        ax = Fx/planet.mass
        ay = Fy/planet.mass

        #Removing planet from planet_list if it goes too far
        if ax < 0.01 and ay < 0.01:
            planet_list.remove(planet)
            continue

        #Determining sign of ax and ay
        if planet.x - star.x > 0:
            ax *= -1
        if planet.y - star.y > 0:
            ay *= -1

        #Adding acceleration to velocity
        planet.x_vel += ax/fps
        planet.y_vel += ay/fps

        #Moving planet with velocity
        planet.x += planet.x_vel/fps
        planet.y += planet.y_vel/fps

        #Checking if planet is selected
        if event.type == pygame.MOUSEBUTTONDOWN:
            if get_dist(mouse_pos[0], mouse_pos[1], planet.x, planet.y) <= 10:
                sel_planet = planet
                selected = True
                p_xy.clear()

        planet.draw()
    star.draw()

    #Displaying total number of planets
    planet_text = planets_font.render(f"Planets in simulation: {len(planet_list)}", True, (255, 255, 255))
    win.blit(planet_text, (width/2 - planet_text.get_width()/2, 0))
    
    #Handling selected planet
    if selected:
        p_xy.append([sel_planet.x, sel_planet.y])
        #Drawing prvious coordinates of selected planet
        while pos_count < len(p_xy):
            x = round(p_xy[pos_count][0])
            y = round(p_xy[pos_count][1])
            n = pos_count * 255/len(p_xy)
            win.set_at((x, y), (n, n, n))
            pos_count += 1
        pos_count = 0

        #Removing old coordinates of selected planet
        if len(p_xy) > 5000:
            p_xy.pop(0)

        #Calculating vel and dist
        vel = round(math.sqrt(sel_planet.x_vel**2 + sel_planet.y_vel**2))
        dist = get_dist(sel_planet.x, sel_planet.y, star.x, star.y)

        #Displaying vel and dist
        stats_text = stats_font.render(f"Instantaneous Velocity: {vel}m/s; Distance from star: {round(dist)}m", True, (255, 255, 255))
        win.blit(stats_text, (width/2 - stats_text.get_width()/2, planet_text.get_height()))

        #Drawing lines and traingle
        pygame.draw.line(win, (255, 243, 0), (sel_planet.x, sel_planet.y), (star.x, star.y), 1)
        pygame.draw.line(win, (255, 243, 0), (sel_planet.x, sel_planet.y), (star.x, sel_planet.y), 1)
        pygame.draw.line(win, (255, 243, 0), (star.x, star.y), (star.x, sel_planet.y), 1)
        pygame.draw.rect(win, (255, 255, 255), (sel_planet.x - 3, sel_planet.y - 3, sel_planet.w + 3, sel_planet.h + 3))

    win.set_at((star.x, star.y), (0, 255, 0))
    pygame.display.update()