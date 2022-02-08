import pygame
import random

nodes = []

height, width = 600, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Path Finder")

class Node:
    def __init__(self, id):
        self.id = id
        self.x = random.randint(10, width - 10)
        self.y = random.randint(10, height - 10)
    def draw(self):
        pygame.draw.rect(win, (0, 0, 255), (self.x - 10, self.y - 10, 10, 10))

for i in range (5):
    node = Node(i+1)
    nodes.append(node)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))

    #Random combination of nodes
    

    #Drawing nodes
    for node in nodes:
        node.draw()

    pygame.display.update()