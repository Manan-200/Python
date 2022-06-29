from combination_gen import comb_arr, NUM
import pygame
import random

pygame.font.init()

#Variables
nodes, node_arr, dist_list = [], [], []
running = True
height, width = 600, 800
dist = 0
fps = 120
main_counter, index_counter= 0, 0
check = False
clicked = False

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
        self.x = random.randint(60, width - 60)
        self.y = random.randint(60, height - 60)
        self.color = (0, 0, 255)
        if self.id == 0 or self.id == NUM + 1:
            self.color = (255, 0, 0)
    def draw(self):
        pygame.draw.rect(win, (self.color), (self.x - 5, self.y - 5, 10, 10))

#Function to create nodes
def create_nodes(n):
    nodes = []
    for i in range(n):
        node = Node(i)
        nodes.append(node)
    return(nodes)

#Creating nodes
nodes = create_nodes(NUM + 2)

#Arranging Nodes in node_arr based on number combinations 
def arrange_nodes(comb_arr):
    node_arr = []
    for id_arr in comb_arr:
        new_arr = []
        for id in id_arr:
            for node in nodes:
                if node.id == id:
                    new_arr.append(node)
        node_arr.append(new_arr)
    return(node_arr)
#Creating combinations
node_arr = arrange_nodes(comb_arr)

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

while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Resetting everything if space is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dist_list, node_arr = [], []
                main_counter, index_counter= 0, 0 
                dist = 0
                nodes = create_nodes(NUM + 2)
                node_arr = arrange_nodes(comb_arr)
        #Setting clicked = True if mouse is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        #Setting clicked = False if mouse is released
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

    win.fill((0, 0, 0))

    main_counter += 1
    
    dist = 0

    #Connecting all combinations of Nodes once
    if index_counter < len(node_arr):
        #Specifying nodes
        nodes = node_arr[index_counter]
        #Connecting nodes with lines and calculating distance
        for p in range(len(nodes) - 1):
            pygame.draw.line(win, (150, 150, 150), (nodes[p].x, nodes[p].y), (nodes[p + 1].x, nodes[p + 1].y))
            dist += get_distance(nodes[p], nodes[p + 1])
        dist_list.append(dist)
        index_counter += 1
    
    #Connecting nodes with minimum distance
    if index_counter >= len(node_arr):
        #Getting minimum index and distance from dist_list
        min_index, min_dist = get_smallest(dist_list)
        #Specifying nodes
        nodes = node_arr[min_index]
        #Connecting nodes with lines
        for p in range(len(nodes) - 1):
            pygame.draw.line(win, (150, 150, 150), (nodes[p].x, nodes[p].y), (nodes[p + 1].x, nodes[p + 1].y))

        dist_text = dist_font.render((f"distance: {round(min_dist)} pixels"), 1, (255, 255, 255))
        win.blit(dist_text, (0, 0))

    for node in nodes:
        selected = False
        #Drawing nodes, blitting distance and id
        id_text = id_font.render(str(node.id), 1, (255, 0, 0))
        node.draw()
        win.blit(id_text, (node.x - (id_text.get_width()/2), node.y - (id_text.get_height()/2) - 12))

        #Changing position of node if it's clickedged with mouse
        mouse_pos = pygame.mouse.get_pos()
        if clicked == True and ((mouse_pos[0] - node.x)**2 + (mouse_pos[1] - node.y)**2 <= 25**2):
            node.x, node.y = mouse_pos[0], mouse_pos[1]
            index_counter = 0
            dist_list = []
            selected = True

    pygame.display.update()

#Checking if the shortest path is correct
if check == True: 
    if (int(input("Check? (1/0)")) == 1):

        test_dist = 0
        test_nodes = []
        id_list = []

        for i in range(len(nodes)):
            id = int(input(f"Enter node id: "))
            id_list.append(id)

        for id in id_list:
            for i in range(len(nodes)):
                if nodes[i].id == id:
                    test_nodes.append(nodes[i])

        for i in range(len(test_nodes) - 1):
            test_dist += get_distance(test_nodes[i], test_nodes[i + 1])

        print(test_dist, min_dist)
        print(len(dist_list), len(node_arr))
        print("\n\n\n", dist_list)