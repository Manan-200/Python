import pygame
import random

fps = 120
obj_list = []
width, height = 1500, 700
G = 6.67 * 10 ** (-11)
main_counter = 0

clock = pygame.time.Clock()

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravity")

class Object:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.accl_x = 0
        self.accl_y = 0
        self.x_vel = 0
        self.y_vel = 0
        self.rad = 1
    def move(self):
        self.x_vel += self.accl_x/fps
        self.y_vel += self.accl_y/fps
        self.x += self.x_vel/fps
        self.y += self.y_vel/fps
    def draw(self):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.rad)

def get_distance(x2, y2, x1, y1):
    a = x2 - x1
    b = y2 - y1
    c = (a**2 + b**2)**0.5
    return c

for i in range(100):
    obj = Object(width/2 + random.randrange(-500, 500), height/2 + random.randrange(-height/2, height/2), random.choice([0.5*10**14, 1*10**14]))
    obj_list.append(obj)

while True:

    main_counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    win.fill((0, 0, 0))

    for obj_1 in obj_list:
        for obj_2 in obj_list:
            if obj_1 != obj_2:

                R = get_distance(obj_1.x, obj_1.y, obj_2.x, obj_2.y)

                if get_distance(obj_1.x, obj_1.y, obj_2.x, obj_2.y) < obj_1.rad + obj_2.rad or R == 0:
                    if obj_1.mass < obj_2.mass:
                        obj_1, obj_2 = obj_2, obj_1
                    obj_1.mass += obj_2.mass
                    obj_1.rad += obj_2.rad*0.5
                    m1, m2 = obj_1.mass, obj_2.mass
                    u1, u2 = obj_1.x_vel, obj_2.x_vel
                    obj_list.remove(obj_2)

                if R != 0:
                    force = G * obj_1.mass * obj_2.mass/R**2

                    obj_1.accl_x = force/obj_1.mass
                    obj_1.accl_y = obj_1.accl_x

                    obj_2.accl_x = force/obj_2.mass
                    obj_2.accl_y = obj_2.accl_x

                    if (obj_1.x) - (obj_2.x) < 0:
                        obj_2.accl_x *= -1
                    if (obj_1.x) - (obj_2.x) > 0:
                        obj_1.accl_x *= -1
                    if (obj_1.y) - (obj_2.y) < 0:
                        obj_2.accl_y *= -1
                    if (obj_1.y) - (obj_2.y) > 0:
                        obj_1.accl_y *= -1

                    obj_1.move()
                    obj_2.move()
                    #print(obj_1.accl_x, obj_1.x_vel)

    for obj in obj_list:
        if get_distance(obj.x, obj.y, width/2, height/2) > width*2:
            obj_list.remove(obj)
        obj.draw()

    pygame.display.update()
    clock.tick(fps)