import pygame
import random

pygame.font.init()

width, height = 1500, 700
fps = 120
xi, yi = 50, -50
x_vel, y_vel, vel = xi, yi, 0
counter, counter_1 = 0, 0
planet_mass = 100
star_mass = 54*(10**15)
G = 6.67 * 10 ** (-11)
R = 0
pos_x_list, pos_y_list = [], []
planet_list = []
planets = 1000
focused_planet = None
barriers = False
movable = False
focussed = False

stats_font = pygame.font.SysFont("calibri", 20)
planets_font = pygame.font.SysFont("calibri", 30)

clock = pygame.time.Clock()

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravity")

def get_distance(x2, y2, x1, y1):
    a = x2 - x1
    b = y2 - y1
    c = (a**2 + b**2)**0.5
    return c

class Planet:
    def __init__(self, x, y, w, h, mass):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.mass = mass
        self.Rect = None
        self.x_vel, self.y_vel = xi, yi

    def draw(self):
        self.Rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(win, (0, 0, 255), self.Rect)

    def move_x(self, vel):
        self.x += vel

    def move_y(self, vel):
        self.y += vel

class Star(Planet):
    def draw(self):
        self.Rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(win, (255, 0, 0), self.Rect) 

if movable:
    for i in range(planets):
        planet = Planet(pygame.mouse.get_pos()[0] + random.randrange(-200, 200), pygame.mouse.get_pos()[1] + random.randrange(-200, 200), 3, 3, planet_mass)
        planet_list.append(planet)
else:
    for i in range(planets):
        planet = Planet(width/10 + random.randrange(-200, 200), height/10 + random.randrange(-200, 200), 3, 3, planet_mass)
        planet_list.append(planet)

pygame.mouse.set_pos(width/2, height/2)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Resetting the variables 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                planets = 1000
                planet_list = []
                vel = 0
                pos_x_list, pos_y_list = [], []
                focussed = False
                c = random.choice([1, 2, 3])
                if c == 2:
                    planets = 10000
                for i in range(planets):
                    if c == 1:
                        coords = width/10 + random.randrange(-200, 200), height/10 + random.randrange(-200, 200)
                    elif c == 2:
                        coords = width/2 + random.randrange(-200, 200), height/2 + random.randrange(-200, 200)
                    elif c == 3:
                        coords = width/10 + random.randrange(-200, 200), 100
                    planet = Planet(coords[0], coords[1], 3, 3, planet_mass)
                    planet_list.append(planet)

    clock.tick(fps)

    counter += 1

    #Filling the screen with color
    win.fill((0, 0, 0))

    #Making star class at mouse pos if movable is true
    if movable:
        star = Star(pygame.mouse.get_pos()[0] - (15/2), pygame.mouse.get_pos()[1] - (15/2), 15, 15, star_mass)
    else:
        star = Star(width/2 - (15/2), height/2 - (15/2), 15, 15, star_mass)
        #star = Star(width - width/5 - (15/2), height - height/5 - (15/2), 15, 15, star_mass)

    #Drawing the star
    star.draw()

    for planet in planet_list:

        #Drawing planet
        planet.draw()

        #Calculating distance, acceleration and force
        R = get_distance(star.x + star.w//2, star.y + star.h//2, planet.x + planet.w//2, planet.y + planet.h//2)
        force = G * star.mass * planet.mass / (R ** 2)
        accl_x = force / planet_mass
        accl_y = force / planet_mass

        #Removing planet if it goes too far
        if accl_x < 0.01 and accl_y < 0.01:
            planet_list.remove(planet)

        #Calculating sign convention of acceleration
        if (star.x + star.w/2) - (planet.x + planet.w/2) < 0:
            accl_x *= -1
        if (star.y + star.h/2) - (planet.y + planet.h/2) < 0:
            accl_y *= -1

        #Bouncing the planet off the walls if barriers are on
        if barriers:
            if planet.x < -500:
                planet.x_vel *= -1
            if planet.x > width + 500:
                planet.x_vel *= -1
            if planet.y < -500:
                planet.y_vel *= -1
            if planet.y > height + 500:
                planet.y_vel *= -1

        #Adding acceleration to velocites on x and y axis per second
        planet.x_vel += accl_x/fps
        planet.y_vel += accl_y/fps

        #Moving the planet per second
        planet.move_x(planet.x_vel/fps)
        planet.move_y(planet.y_vel/fps)

    #Displaying stats 1
    planet_text = planets_font.render((f"Number of planets : {len(planet_list)}"), 1, (255, 255, 255))
    win.blit(planet_text, (width/2 - planet_text.get_width()/2, 0))

    #Focusing on a single planet
    #Choosing a planet when clicking on it
    for planet in planet_list:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] > planet.x - 5 and mouse_pos[0] < planet.x + planet.w + 5 and mouse_pos[1] > planet.y - 5 and mouse_pos[1] < planet.y + planet.h + 5:
                pos_x_list.clear()
                pos_y_list.clear()
                focused_planet = planet
                focussed = True
                break
    if focussed:
        #Drawing planet outline and line
        pygame.draw.rect(win, (255, 255, 255), (focused_planet.x - 1, focused_planet.y - 1, focused_planet.w + 1, focused_planet.h + 1), 1)
        pygame.draw.line(win, (255, 255, 255), (focused_planet.x + focused_planet.w/2, focused_planet.y + focused_planet.h/2), (star.x + star.w/2, star.y + star.h/2), 1)

        #Calculating velocity
        pos_x_list.append(focused_planet.x)
        pos_y_list.append(focused_planet.y)
        if len(pos_x_list) > 5000 and len(pos_y_list) > 5000:
            pos_x_list.remove(pos_x_list[0])
            pos_y_list.remove(pos_y_list[0])
        if len(pos_x_list) >= 2 and len(pos_y_list) >= 2:
            vel = round(get_distance(pos_x_list[-1], pos_y_list[-1], pos_x_list[-2], pos_y_list[-2]) * fps)

        #Drawing focussed planet's path
        while counter_1 != len(pos_x_list) and counter_1 != len(pos_y_list):
            x = round(pos_x_list[counter_1])
            y = round(pos_y_list[counter_1])
            n = counter_1 * 255/len(pos_x_list)
            win.set_at((x, y), (n, n, n))
            counter_1 += 1
        counter_1 = 0

        #Displaying stats 2
        dist = get_distance(star.x + star.w//2, star.y + star.h//2, focused_planet.x + focused_planet.w//2, focused_planet.y + focused_planet.h//2)
        stats_text = stats_font.render((f"distance from star : {round(dist)}m ; Instantaneous velocity : {round(vel)}m/s"), 1, (255, 255, 255))
        win.blit(stats_text, (width/2 - stats_text.get_width()/2, planet_text.get_height()))

    pygame.display.update()