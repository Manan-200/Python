import pygame

pygame.font.init()

width, height = 1500, 700
fps = 120
xi, yi = 100, -100
x_vel, y_vel, vel = xi, yi, 0
counter = 0
planet_mass = 100
star_mass = 12*(10**16)
G = 6.67 * 10 ** (-11)
R = 0
pos_x_list, pos_y_list = [], []
barriers = False
movable = True

stats_font = pygame.font.SysFont("calibri", 30)

clock = pygame.time.Clock()

win = pygame.display.set_mode((width, height))

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

if movable:
    planet = Planet(pygame.mouse.get_pos()[0] + 200, pygame.mouse.get_pos()[1] + 200, 5, 5, planet_mass)
else:
    planet = Planet(width/2 + 200, height/2 + 200, 5, 5, planet_mass)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        #Resetting the variables 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                planet.x, planet.y = pygame.mouse.get_pos()[0] + 200, pygame.mouse.get_pos()[1] + 200
                x_vel, y_vel = xi, yi
                vel = 0
                pos_x_list, pos_y_list = [], []

    clock.tick(fps)

    counter += 1

    #Filling the screen with color
    win.fill((50, 50, 50))

    #Making star class at mouse pos if movable is true
    if movable:
        star = Star(pygame.mouse.get_pos()[0] - 12.5, pygame.mouse.get_pos()[1] - 12.5, 25, 25, star_mass)
    else:
        star = Star(width/2 - 12.5, height/2 - 12.5, 25, 25, star_mass)

    #Drawing planet and star
    planet.draw()
    star.draw()

    #Calculating distance, acceleration and force
    R = get_distance(star.x + star.w//2, star.y + star.h//2, planet.x + planet.w//2, planet.y + planet.h//2)
    force = G * star.mass * planet.mass / (R ** 2)
    accl_x = force / planet_mass
    accl_y = force / planet_mass

    #Calculating velocity
    pos_x_list.append(planet.x)
    pos_y_list.append(planet.y)
    if len(pos_x_list) > 3 and len(pos_y_list) > 3:
        pos_x_list.remove(pos_x_list[0])
        pos_y_list.remove(pos_y_list[0])
    if len(pos_x_list) >= 2 and len(pos_y_list) >= 2:
        vel = round(get_distance(pos_x_list[-1], pos_y_list[-1], pos_x_list[-2], pos_y_list[-2]))

    #Calculating sign convention of acceleration
    if (star.x + star.w/2) - (planet.x + planet.w/2) < 0:
        accl_x *= -1
    if (star.y + star.h/2) - (planet.y + planet.h/2) < 0:
        accl_y *= -1

    #Bouncing the planet off the walls if barriers are on
    if barriers:
        if planet.x < -500:
            x_vel *= -1
        if planet.x > width + 500:
            x_vel *= -1
        if planet.y < -500:
            y_vel *= -1
        if planet.y > height + 500:
            y_vel *= -1

    #Adding acceleration to velocites on x and y axis per second
    x_vel += accl_x/fps
    y_vel += accl_y/fps

    #Moving the planet per second
    planet.move_x(x_vel/fps)
    planet.move_y(y_vel/fps)

    #Displaying statistics
    stats_text = stats_font.render((f"x_vel : {round(x_vel)} pixels/s ; y_vel : {round(y_vel)} pixels/s ; distance : {round(R)} m ; velocity : {vel} m/s"), 1, (255, 255, 255))
    win.blit(stats_text, (width/2 - stats_text.get_width()/2, 0))

    pygame.display.update()