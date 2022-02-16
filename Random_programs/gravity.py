import pygame
pygame.font.init()

width, height = 1500, 700
fps = 120
x_vel, y_vel, vel = 150, 50, 0
counter = 0
collided = False
planet_mass = 6*(10)
star_mass = 12*(10**14)
G = 6.67 * 10 ** (-11)
R = 0
pos_x_list, pos_y_list = [], []

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

planet = Planet(0, height//2, 5, 5, planet_mass)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        #Resetting the variables 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                collided = False
                planet.x, planet.y = 0, height//2
                x_vel, y_vel = 150, 50

    clock.tick(fps)

    counter += 1

    #Filling the screen with color
    win.fill((50, 50, 50))

    #Making star class at mouse pos
    star = Star(pygame.mouse.get_pos()[0] - 12.5, pygame.mouse.get_pos()[1] - 12.5, 25, 25, star_mass)

    #Drawing planet and star
    if collided == False:
        planet.draw()
    star.draw()

    #Calculating distance, acceleration and force
    R = get_distance(star.x + star.w//2, star.y + star.h//2, planet.x + planet.w//2, planet.y + planet.h//2)
    force = G * star.mass * planet.mass / (R ** 2)
    accl_x = force / planet_mass
    accl_y = force / planet_mass

    #Calculating velocity
    if counter % fps == 0 and collided == False:
        pos_x_list.append(planet.x)
        pos_y_list.append(planet.y)
    if len(pos_x_list) > 2 and len(pos_y_list) > 2:
        pos_x_list.remove(pos_x_list[-1])
        pos_y_list.remove(pos_y_list[-1])
    if len(pos_x_list) > 2 and len(pos_y_list) > 0:
        vel = get_distance(pos_x_list[1], pos_y_list[1], pos_x_list[0], pos_y_list[0])

    #Calculating sign convention of acceleration
    if (star.x + star.w/2) - (planet.x + planet.w/2) < 0:
        accl_x *= -1
    if (star.y + star.h/2) - (planet.y + planet.h/2) < 0:
        accl_y *= -1

    #Checking for collision
    if planet.Rect.colliderect(star.Rect):
        collided = True

    #Bouncing the planet off the walls
    if planet.x < -500:
        x_vel *= -1
    if planet.x > width + 500:
        x_vel *= -1
    if planet.y < -500:
        y_vel *= -1
    if planet.y > height + 500:
        y_vel *= -1

    #Adding acceleration to velocites on x and y axis
    x_vel += accl_x
    y_vel += accl_y

    #Moving the planet
    planet.move_x(x_vel/fps)
    planet.move_y(y_vel/fps)

    #Displaying statistics
    stats_text = stats_font.render((f"x_vel : {round(x_vel)}m/s ; y_vel : {round(y_vel)}m/s ; distance : {round(R)} ; velocity : {vel}"), 1, (255, 255, 255))
    win.blit(stats_text, (width - stats_text.get_width(),0))

    pygame.display.update()