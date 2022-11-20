import pygame
import json
import random

width, height = 700, 500
box_vel = 5
clock = pygame.time.Clock()
fps = 120
box_arr = []

DATA_FILE = "client_data.json"

window = pygame.display.set_mode((width, height))

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f)
def load_data(file):
    try:
        with open(file, "r") as f:
            return(json.load(f))
    except:
        return {}

class Box:
    def __init__(self, x=width/2, y=height/2):
        self.x = x
        self.y = y
        self.w = 25
        self.h = 25
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def draw(self):
        self.Rect = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        pygame.draw.rect(window, self.color, self.Rect)

box = Box()

run = True
while run:

    clock.tick(fps)

    data = load_data(DATA_FILE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and box.x - box.w/2 > 0:
        box.x -= box_vel
    if keys[pygame.K_d] and box.x + box.w/2 < width:
        box.x += box_vel
    if keys[pygame.K_w] and box.y - box.h/2 > 0:
        box.y -= box_vel
    if keys[pygame.K_s] and box.y + box.h/2 < height:
        box.y += box_vel
    
    for addr in data:
        if addr != "self" and addr != "state":
            x = data[addr][0]
            y = data[addr][1]
            box2 = Box(x, y)
            box2.draw()
            
    box.draw()
    data["self"] = [box.x, box.y]
    save_data(DATA_FILE, data)

    pygame.display.update()