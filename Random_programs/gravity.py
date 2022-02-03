import pygame
pygame.font.init()

width, height = 1500, 700
fps = 120
x_vel, y_vel = 200, 0
counter = 0
planet_mass = 6*(10**9)
star_mass = 6*(10**18)
x_list, y_list = [], []
G = 6.67 * 10 ** (-11)
R = 0

vel_font = pygame.font.SysFont("calibri", 30)

clock = pygame.time.Clock()

win = pygame.display.set_mode((width, height))

class Planet:
    def __init__(self, x, y, w, h, mass):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.mass = mass
        self.Rect = None

    def draw(self):
        self.Rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(win, (255, 0, 0), self.Rect)

    def move_x(self, vel):
        self.x += vel

    def move_y(self, vel):
        self.y += vel

class Star(Planet):
    def draw(self):
        self.Rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(win, (0, 0, 255), self.Rect)

planet = Planet(0, height//2, 5, 5, planet_mass)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                planet.x, planet.y = 0, height//2
                x_vel, y_vel = 200, 0

    clock.tick(fps)

    counter += 1

    vel_text = vel_font.render((f"x_vel : {round(x_vel)}m/s ; y_vel : {round(y_vel)}m/s ; distance : {round(R)}"), 1, (255, 255, 255))

    win.fill((50, 50, 50))

    star = Star(pygame.mouse.get_pos()[0] - 12.5, pygame.mouse.get_pos()[1] - 12.5, 25, 25, star_mass)

    planet.draw()
    star.draw()
    win.blit(vel_text, (width - vel_text.get_width(),0))
    x_list.append(planet.x + planet.w/2)
    y_list.append(planet.y + planet.h/2)

    #win.fill((255, 255, 255), ((planet.x, planet.y), (1, 1)))

    R = (((star.x + star.w) - planet.x)**2 + ((star.y + star.h) - planet.y)**2)*(1/2)
    accl = G * star.mass / R ** 2
    
    if planet.x - (star.x + star.w/2) < 0:
            x_vel += accl
    if planet.x - (star.x + star.w/2) > 0:
            x_vel -= accl
    if planet.y - (star.y + star.h/2) < 0:
            y_vel += accl
    if planet.y - (star.y + star.h/2) > 0:
            y_vel -= accl

    if planet.x > width + 200:
        x_vel *= -1
    if planet.x < -200:
        x_vel *= -1
    if planet.y > height + 200:
        y_vel *= -1
    if planet.y < -200:
        y_vel *= -1

    planet.move_x(x_vel/fps)
    planet.move_y(y_vel/fps)    

    pygame.display.update()