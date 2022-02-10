import pygame
import random

#Variables
nodes, num_list, new_list = [], [], []
running = True
height, width = 600, 800
dist = 0
counter_1, counter_2 = 0, 0

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Path Finder")

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
                        num_list.append([a, b, c, d, e])

#Function for calculation distance between two nodes
def distance(node_1, node_2):
    distance = ((node_1.x - node_2.x)**2 + (node_1.y - node_2.y)**2) ** (1/2)
    return distance

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(dist)

    win.fill((0, 0, 0))

    #Drawing nodes
    for node in nodes:
        node.draw()

    #Generating combinations of nodes and adding in new_list
    for num1 in num_list:
        for num2 in num1:
            for node in nodes:
                if num2 == node.id and counter_1 != 120:
                    counter_1 += 1
                    new_list.append([node])

    #Calculating distance between nodes
    for j in new_list:
        for i in range(len(j)):
            if counter_2 != 120:
                counter_2 += 1
                if i < 5:
                    dist += round(distance(j[i], j[i+1]))
                elif i == 5:
                    dist += round(distance(j[i - 1], j[i]))

    pygame.display.update()