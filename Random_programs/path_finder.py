from re import X
import pygame
import random

pygame.font.init()

#Variables
nodes, c_arr, node_arr, dist_list, node_f = [], [], [], [], []
running = True
height, width = 600, 800
dist = 0
min_display_dist, max_display_dist = 0, 0
fps = 15
main_counter, index_counter, draw_counter = 0, 0, 0

#Clock
clock = pygame.time.Clock()

#Window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Path Finder")

#Font for displaying distance
dist_font = pygame.font.SysFont("comicsans", 15)
id_font = pygame.font.SysFont("comicsans", 10)

#Node class
class Node:
    def __init__(self, id):
        self.id = id
        if self.id != 0:
            self.x = random.randint(10, width - 10)
            self.y = random.randint(10, height - 10)
        elif self.id == 0:
            self.x = 100
            self.y = 100
    def draw(self):
        pygame.draw.rect(win, (0, 0, 255), (self.x - 5, self.y - 5, 10, 10))

#Creating nodes

for i in range (5):
    node = Node(i+1)
    nodes.append(node)
node_0 = Node(0)
#Making all combination of nodes
for a in range (1,6):
    for b in range (1,6):
        for c in range (1,6):
            for d in range (1,6):
                for e in range (1,6):
                    if a + b + c + d + e == 15 and a*b*c*d*e == 120:
                        c_arr.append([a, b, c, d, e])

#Function for calculation distance between two nodes
def get_distance(node_1, node_2):
    distance = ((node_1.x - node_2.x)**2 + (node_1.y - node_2.y)**2) ** (1/2)
    return(distance)

def get_smallest(arr):
    min_val = arr[0]
    min_index = 0
    if len(arr) > 0:
        for i in range(len(arr)):
                if arr[i] < min_val:
                    min_val = arr[i]
                    min_index = i
        return([min_index, min_val])

for id_arr in c_arr:
    new_arr = []
    for id in id_arr:
        for node in nodes:
            if node.id == id:
                new_arr.append(node)
    node_arr.append(new_arr)

while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    index_counter += 1
    main_counter += 1
    win.fill((0, 0, 0))
    dist = 0

    if index_counter >= len(node_arr):
        index_counter = 0

    nodes = node_arr[index_counter]

    if draw_counter <= len(node_arr):
        for p in range(len(nodes) - 1):
            pygame.draw.line(win, (150, 150, 150), (nodes[p].x, nodes[p].y), (nodes[p + 1].x, nodes[p + 1].y))
            dist += get_distance(nodes[p], nodes[p + 1])
            draw_counter += 1
        dist += get_distance(nodes[0], node_0)
        pygame.draw.line(win, (150, 150, 150), (nodes[0].x, nodes[0].y), (node_0.x, node_0.y))
        dist_list.append(dist)
    
    if draw_counter > len(node_arr):
        min_index, min_dist = get_smallest(dist_list)
        nodes = node_arr[min_index]
        for p in range(len(nodes) - 1):
            pygame.draw.line(win, (150, 150, 150), (nodes[p].x, nodes[p].y), (nodes[p + 1].x, nodes[p + 1].y))
        pygame.draw.line(win, (150, 150, 150), (nodes[0].x, nodes[0].y), (node_0.x, node_0.y))
        dist_text = dist_font.render((f"distance: {round(min_dist)} pixels"), 1, (255, 255, 255))
        win.blit(dist_text, (0, 0))

    for node in nodes:
        id_text = id_font.render(str(node.id), 1, (255, 0, 0))
        node.draw()
        win.blit(id_text, (node.x - (id_text.get_width()/2), node.y - (id_text.get_height()/2) - 10))
    node_0.draw()
    id_text = id_font.render(str(node_0.id), 1, (255, 0, 0))
    win.blit(id_text, (node_0.x - (id_text.get_width()/2), node_0.y - (id_text.get_height()/2) - 10))

    pygame.display.update()