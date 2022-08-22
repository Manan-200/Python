import pygame
import random

width, height = 500, 300
win = pygame.display.set_mode((width, height))

x, y, z = 0, 0, 0
counter = 0
z_list = []

def colour(z):
    ground = (155, 118, 83)
    ocean = (0, 105, 148)
    forest = (31, 61, 12)
    if z > 0 and z <= 0.00005:
        colour = ground
    elif z > 0.00005:
        colour = forest
    elif z <= 0:
        colour = ocean
    return(colour)

for x in range(width):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    for y in range(height):
        counter += 1
        if x > 0:
            w1 = z_list[- height + 1]
        else:
            w1 = 0
        z = (random.randrange(-1, 2)*0.0002/10 + z*4.9999/10 + w1*4.9999/10)
        z_list.append(z)
        while len(z_list) > 2*height:
            z_list.pop(0)
        win.set_at((x, y), colour(z))
        pygame.display.update()