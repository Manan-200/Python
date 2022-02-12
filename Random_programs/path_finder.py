import pygame
import random

pygame.font.init()

#Variables
nodes, combination_list, node_combination, distance_list = [], [], [], []
running = True
height, width = 600, 800
dist = 0
counter_1, counter_2 = 1, 0
fps = 60
counter = 0

#Clock
clock = pygame.time.Clock()

#Window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Path Finder")

#Font for displaying distance
dist_font = pygame.font.SysFont("comicsans", 25)

#Node class
class Node:
    def __init__(self, id):
        self.id = id
        self.x = random.randint(10, width - 10)
        self.y = random.randint(10, height - 10)
    def draw(self):
        pygame.draw.rect(win, (0, 0, 255), (self.x - 10, self.y - 10, 10, 10))

#Creating nodes
for i in range (5):
    node = Node(i+1)
    nodes.append(node)


#Making all combination of nodes
for a in range (1,6):
    for b in range (1,6):
        for c in range (1,6):
            for d in range (1,6):
                for e in range (1,6):
                    if a + b + c + d + e == 15 and a*b*c*d*e == 120:
                        combination_list.append([a, b, c, d, e])

#Function for calculation distance between two nodes
def distance(node_1, node_2):
    distance = ((node_1.x - node_2.x)**2 + (node_1.y - node_2.y)**2) ** (1/2)
    return distance

while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(dist)

    counter += 1

    win.fill((0, 0, 0))
            
    #Making node_combination
    num1 = combination_list[counter_1 - 1]
    for num2 in num1:
        for node in nodes:
            if node.id == num2 and len(node_combination) != 5:
                node_combination.append(node)

    #Clearing node_combination after every 5 steps
    if len(node_combination) == 5 and counter%5 == 0:
        counter_1 += 1
        node_combination.clear()

    #Calculating distance
    for i in range(len(node_combination)):
        if i < 4:
            dist += distance(node_combination[i], node_combination[i+1])
        elif i == 4:
            dist += distance(node_combination[i], node_combination[0])
    distance_list.append(dist)
    dist = min(distance_list)

    #Drawing nodes
    for node in nodes:
        node.draw()

    #Displaying distance
    dist_text = dist_font.render(f"Distance : {round(dist)}", 1, (255, 255, 255))
    win.blit(dist_text, (width - dist_text.get_width() - 10, 10))

    pygame.display.update()