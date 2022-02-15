import pygame
import random

pygame.font.init()

#Variables
nodes, nodes2, combination_list, node_combination, distance_list = [], [], [], [], []
running = True
height, width = 600, 800
dist = 0
min_display_dist, max_display_dist = 0, 0
counter_1 = 1
fps = 60
counter = 0

#Clock
clock = pygame.time.Clock()

#Window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Path Finder")

#Font for displaying distance
dist_font = pygame.font.SysFont("comicsans", 25)
id_font = pygame.font.SysFont("comicsans", 10)

#Node class
class Node:
    def __init__(self, id):
        self.id = id
        self.x = random.randint(10, width - 10)
        self.y = random.randint(10, height - 10)
    def draw(self):
        pygame.draw.rect(win, (0, 0, 255), (self.x - 5, self.y - 5, 10, 10))

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
        #Resetting everything after pressing spacebar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                nodes, nodes2, node_combination, distance_list = [], [], [], []
                counter_1, counter = 1, 0
                dist = 0
                running = True
                for i in range (5):
                    node = Node(i+1)
                    nodes.append(node)

    counter += 1

    win.fill((0, 0, 0))

    #Drawing nodes
    for node in nodes:
        id_text = id_font.render(str(node.id), 1, (255, 0, 0))
        node.draw()
        win.blit(id_text, (node.x - id_text.get_width()/2, node.y - 10 - id_text.get_height()/2))
        print(f"Node {node.id} is at ({node.x}, {node.y})")
            
    #Making node_combination
    var1 = combination_list[counter_1 - 1]
    for var2 in var1:
        for node in nodes:
            if node.id == var2 and len(node_combination) != 5:
                node_combination.append(node)
    if len(nodes2) <= 120:
        nodes2.append(node_combination)

    #Is implemented after every 2 steps
    if counter % 2 == 0:
        
        if counter <= 120:
            counter_1 += 1

        #Calculating distance between nodes
        for i in range(len(node_combination)):
            if i < 4:
                dist += distance(node_combination[i], node_combination[i+1])
            elif i == 4:
                dist += distance(node_combination[i], node_combination[0])
        distance_list.append(dist)
        dist = 0

        #Getting minimum and maximum distance
        max_display_dist = max(distance_list)
        min_display_dist = min(distance_list)

        #Connecting nodes with lines
        var3 = nodes2[distance_list.index(min_display_dist)]
        for j in range(len(var3)):
            if j < 4:
                pygame.draw.line(win, (255, 255, 255), (var3[j].x, var3[j].y), (var3[j+1].x, var3[j+1].y), 1)
            elif j == 4:
                pygame.draw.line(win, (255, 255, 255), (var3[j].x, var3[j].y), (var3[0].x, var3[0].y), 1)

        #Clearing node_combination
        node_combination.clear()

    #Displaying distance
    min_dist_text = dist_font.render(f"Minimum distance : {round(min_display_dist)}", 1, (255, 255, 255))
    win.blit(min_dist_text, (width - min_dist_text.get_width() - 10, 10))

    pygame.display.update()