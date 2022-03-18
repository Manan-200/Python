from tkinter import W
import pygame
import os
import random

pygame.font.init() #Initializing fonts

#Variables
width, height = 1000, 600
player_vel = 3
bg_x, bg_y = -500, -500
fps = 60
rock_w, rock_h = 50, 50
tree_w, tree_h = 75, 120
rock_list, tree_list, zombie_list = [], [], []
all_items_dict = {"rock": 0, "wood": 0, "food": 0}
inventory_dict = {}
drop_list = []
inventory_state = False
index_counter = 1
main_counter = 0
spawn_cycle = 1
hunger_reduction = 0.01
clock = pygame.time.Clock()
o1, o2, o3, o4 = False, False, False, False

#Fonts
inventory_font = pygame.font.SysFont("calibri", 11)
stats_font = pygame.font.SysFont("calibri", 15)

#Window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Indie Game")

#Player image
player_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_img.png")) , (25 * 1.5, 136/4 * 1.5))

#Zombie image
zombie_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "zombie_img.png")), (161 * 25*1.5/161, 239 * 25*1.5/161))

#Background image
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img.png")), (width + 2*(-bg_x), height + 2*(-bg_y)))

#Rock images
rock_img_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_1.png")), (rock_w, rock_h))
rock_img_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_2.png")), (rock_w, rock_h))
rock_img_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_3.png")), (rock_w, rock_h))
rock_img_4 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_4.png")), (rock_w, rock_h))
rock_img_5 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_5.png")), (rock_w, rock_h))
rock_img_6 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_6.png")), (rock_w + 25, rock_h + 25))
rock_img_7 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_7.png")), (rock_w + 25, rock_h + 25))

#Tree images
tree_img_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_1.png")), (tree_w, tree_h))
tree_img_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_2.png")), (tree_w, tree_h))
tree_img_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_3.png")), (59 * 2, 75 * 2))
tree_img_4 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_4.png")), (45 * 2, 69 * 2))
#tree_img_5 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_5.png")), (tree_w, tree_h))
#tree_img_6 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_6.png")), (tree_w, tree_h))

#Drop images
wood_drop_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "wood_drop_img.png")), (77, 31))
rock_drop_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_drop_img.png")), (45 * 1.5, 20 * 2))

#Images for inventory
inventory_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "inventory_img.png")), (706, 482))
inventory_wood_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "wood_drop_img.png")), (77/1.5, 31/1.5))
inventory_rock_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_drop_img.png")), (45 * 1.5/1.5, 20 * 2))

#Removing unnecessary white background
rock_img_1.set_colorkey((255, 255, 255))
rock_img_2.set_colorkey((246, 246, 246))
rock_img_3.set_colorkey((255, 255, 255))
rock_img_4.set_colorkey((220, 240, 244))
rock_img_5.set_colorkey((220, 240, 244))
rock_img_6.set_colorkey((220, 240, 244))
rock_img_7.set_colorkey((220, 240, 244))

tree_img_1.set_colorkey((255, 255, 255))
tree_img_2.set_colorkey((255, 255, 255))
tree_img_3.set_colorkey((255, 255, 255))
tree_img_4.set_colorkey((255, 255, 255))
#tree_img_5.set_colorkey((255, 255, 255))
#tree_img_6.set_colorkey((255, 255, 255))

wood_drop_img.set_colorkey((255, 255, 255))
rock_drop_img.set_colorkey((255, 255, 255))

player_img.set_colorkey((255, 255, 255))

zombie_img.set_colorkey((255, 255, 255))

inventory_wood_img.set_colorkey((255, 255, 255))
inventory_rock_img.set_colorkey((255, 255, 255))

def handle_collisions(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    if obj1.mask.overlap(obj2.mask, (offset_x, offset_y)):
        return True  

def get_distance(x2, y2, x1, y1):
    a = x2 - x1
    b = y2 - y1
    c = (a**2 + b**2)**0.5
    return c

#Player object
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = player_img
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.mask = pygame.mask.from_surface(self.img)
        self.health = 100
        self.hunger = 100
    def draw(self):
        self.Rect = pygame.Rect(self.x, self.y, self.w, self.h)
        win.blit(self.img, (self.x, self.y)) #Drawing player
        self.healthRect_1 = pygame.Rect(self.x, self.y + self.h + 3, self.w, 2.5)
        self.healthRect_2 = pygame.Rect(self.x, self.y + self.h + 3, self.w * self.health/100, 2.5)
        self.hungerRect_1 = pygame.Rect(self.x, self.y + self.h + self.healthRect_1.h + 5, self.w, 2.5)
        self.hungerRect_2 = pygame.Rect(self.x, self.y + self.h + self.healthRect_1.h + 5, self.w * self.hunger/100, 2.5)

        pygame.draw.rect(win,(255, 0, 0), self.hungerRect_1) 
        pygame.draw.rect(win, (255, 255, 0), self.hungerRect_2) #Drawing hunger bar
        pygame.draw.rect(win, (255, 0, 0), self.healthRect_1)
        pygame.draw.rect(win, (0, 255, 0), self.healthRect_2) #Drawing health bar

#Zombie object
class Zombie:
    def __init__(self):
        self.x = random.randrange(1, bg_img.get_width() - 50)
        self.y = random.randrange(1, bg_img.get_height() - 50)
        self.img = zombie_img
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.mask = pygame.mask.from_surface(self.img)
        self.health = 100
    def draw(self):
        self.Rect = pygame.Rect(self.x + bg_x, self.y + bg_y, self.w, self.h)
        win.blit(self.img, (self.Rect.x, self.Rect.y)) #Drawing zombie
    def move(self, player):
        if self.Rect.x < player.x:
            self.x += 1
        if self.Rect.y < player.y:
            self.y += 1
        if self.Rect.x > player.x:
            self.x -= 1
        if self.Rect.y > player.y:
            self.y -= 1

#Rock object
class Rock:
    def __init__(self):
        self.x = random.randrange(1, bg_img.get_width() - 50)
        self.y = random.randrange(1, bg_img.get_height() - 50)
        self.img = random.choice([rock_img_4, rock_img_5, rock_img_6, rock_img_7])
        self.drops = random.randrange(3, 5)
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.mask = pygame.mask.from_surface(self.img)
        self.strength = random.randrange(50, 60)
    def draw(self):
        win.blit(self.img, (bg_x + self.x, bg_y + self.y))
        self.Rect = pygame.Rect(bg_x + self.x, bg_y + self.y, self.w, self.h)

#Tree object
class Tree:
    def __init__(self):
        self.x = random.randrange(1, bg_img.get_width() - 50)
        self.y = random.randrange(1, bg_img.get_height() - 50)
        self.img = random.choice([tree_img_1, tree_img_2, tree_img_3, tree_img_4])
        self.drops = random.randrange(3, 5)
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.mask = pygame.mask.from_surface(self.img)
        self.strength = random.randrange(50, 60)
    def draw(self):
        win.blit(self.img, (bg_x + self.x, bg_y + self.y))
        self.Rect = pygame.Rect(bg_x + self.x, bg_y + self.y, self.w, self.h)

#Drop object
class Drop:
    def __init__(self, x, y, h, type):
        self.x = x
        self.type = type
        if self.type == "wood":
            self.img = wood_drop_img
            self.y = y + h/2
        elif self.type == "rock":
            self.img = rock_drop_img
            self.y = y + h/4
        self.w = self.img.get_width()
        self.h = self.img.get_height()
    def draw(self):
        win.blit(self.img, (bg_x + self.x, bg_y + self.y))

#Creating player object
player = Player(width/2, height/2)

"""
MAIN LOOP
"""
running = True
while running:

    main_counter += 1

    #Quitting the game if cross button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Filling window with black color
    win.fill((200, 200, 200))

    #Drawing background
    win.blit(bg_img, (bg_x, bg_y))
    
    #Detecting keys pressed
    keys = pygame.key.get_pressed()
    if inventory_state == False:
        #Basic movements
        if keys[pygame.K_a] and player.x > bg_x and o1 == False:
            bg_x += player_vel
            player.hunger -= hunger_reduction
        if keys[pygame.K_d] and player.x + player.h < bg_x + bg_img.get_width() and o2 == False:
            bg_x -= player_vel
            player.hunger -= hunger_reduction
        if keys[pygame.K_w] and player.y > bg_y and o3 == False:
            bg_y += player_vel
            player.hunger -= hunger_reduction
        if keys[pygame.K_s] and player.y + player.h < bg_y + bg_img.get_height() and o4 == False:
            bg_y -= player_vel
            player.hunger -= hunger_reduction
        #Increasing speed of player if ctrl is pressed
        if keys[pygame.K_LCTRL] and player.hunger > 0:
            player_vel = 6
            hunger_reduction = 0.02
        elif player.hunger > 0:
            player_vel = 3
            hunger_reduction = 0.01

    #Reducing player's speed if hunger is 0
    if player.hunger <= 0:
        player_vel = 1

    #Things to be done per second
    if main_counter % fps == 0:
        player.hunger -= 0.001 #Decreasing hunger
        if player.hunger <= 0:
            player.hunger = 0
            player.health -= 1 #Decreasing health if hunger is 0
        if player.health <= 0:
            player.health = 0
            running = False #Quitting the game if health is 0

    #Keys for showing inventory
    if keys[pygame.K_e]:
        inventory_state = True
    if keys[pygame.K_ESCAPE]:
        inventory_state = False
    
    #Adding items in inventory_dict from all_items_dict if its value is greater than 0
    for item in all_items_dict:
        if all_items_dict[item] > 0:
            inventory_dict[item] = all_items_dict[item]

    #Creating zombie, rock and tree objects
    while len(rock_list) != 25 and spawn_cycle == 1:
        rock = Rock()
        rock_list.append(rock)
    while len(tree_list) != 25 and spawn_cycle == 1:
        tree = Tree()
        tree_list.append(tree)
    while len(zombie_list) != 10 and spawn_cycle == 1:
        zombie = Zombie()
        zombie_list.append(zombie)

    #Getting postion of mouse
    mouse_pos = pygame.mouse.get_pos()

    #Resetting obstacle states
    o1, o2, o3, o4 = False, False, False, False

    #Handling zombies
    for zombie in zombie_list:
        #Drawing zombie
        zombie.draw()
        #Moving zombie if its disyance from player is smaller than 200
        if get_distance(player.x, player.y, zombie.Rect.x, zombie.Rect.y) < width/2:
            zombie.move(player)
        #Reducing player's health if zombie is touching player per second
        if get_distance(player.x, player.y, zombie.Rect.x, zombie.Rect.y) < 50 and main_counter % fps == 0:
            player.health -= random.randrange(1, 10)
        #Reducing zombie's health if mouse is clicked on zombie
        if zombie.Rect.collidepoint(mouse_pos) and get_distance(player.x, player.y, zombie.Rect.x, zombie.Rect.y) < 70 and main_counter % fps == 0:
            zombie.health -= random.randrange(30, 50)
        #Removing zombie if its health is 0
        if zombie.health <= 0:
            zombie_list.remove(zombie)

    #Handling rocks
    for rock in rock_list:
        #Drawing rocks
        rock.draw()
        #Reducing rock's strength if player is near it and mouse is clicked on rock
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos[0] > rock.Rect.x and mouse_pos[0] < rock.Rect.x + rock.Rect.w and mouse_pos[1] > rock.Rect.y and mouse_pos[1] < rock.Rect.y + rock.Rect.h:
                if get_distance(player.x + player.w/2, player.y + player.h/2, rock.Rect.x + rock.w/2, rock.Rect.y + rock.h/2) < 75:
                    rock.strength -= 1
        #Adding rock to drop_list and removing it from rock_list if its strength is 0                    
        if rock.strength == 0:
            for i in range(rock.drops):
                drop = Drop(rock.x, rock.y + i*5, rock.h, "rock")
                drop_list.append(drop)
            rock_list.remove(rock)

    #Handling trees
    for tree in tree_list:
        #Drawing trees
        tree.draw()
        #Reducing tree's strength if player is near it and mouse is clicked on tree
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos[0] > tree.Rect.x and mouse_pos[0] < tree.Rect.x + tree.Rect.w and mouse_pos[1] > tree.Rect.y and mouse_pos[1] < tree.Rect.y + tree.Rect.h:
                if get_distance(player.x + player.w/2, player.y + player.h/2, tree.Rect.x + tree.w/2, tree.Rect.y + tree.h*3/4) < 50:
                    tree.strength -= 1
        #Adding tree to drop_list and removing it from tree_list if its strength is 0
        if tree.strength == 0:
            for i in range(tree.drops):
                drop = Drop(tree.x, tree.y + i*10, tree.h, "wood")
                drop_list.append(drop)
            tree_list.remove(tree)

    #Handling drops
    for drops in drop_list:
        #Drawing drops
        drops.draw()
        #Updating value of drop in all_items_dict and removing it from drop_list if player is near it
        if get_distance(player.x + player.w/2, player.y + player.h/2, drops.x + drops.w/2 + bg_x, drops.y + drops.h/2 + bg_y) < 20:
            if drop.type == "wood":
                all_items_dict["wood"] += 1
            elif drop.type == "rock":
                all_items_dict["rock"] += 1
            drop_list.remove(drops)

    #Drawing player
    player.draw()

    #Handling inventory
    if inventory_state:
        #Drawing inventory
        inventoryRect = pygame.Rect(100, 100, width - inventory_img.get_width()/2, height - inventory_img.get_height()/2)
        win.blit(inventory_img, (inventoryRect.x, inventoryRect.y))
        
        #Handling items on inventory menu
        for item in inventory_dict:
            if item == "wood":
                item_img = inventory_wood_img
            elif item == "rock":
                item_img = inventory_rock_img
            item_text = inventory_font.render(str(inventory_dict[str(item)]), 1, (255, 255, 255)) #Text of number of items
            item_x, item_y = inventoryRect.x + 252.5, inventoryRect.y + 3 + (index_counter * 55)
            inventory_img.blit(item_img, (item_x, item_y)) #Drawing items
            inventory_img.blit(item_text, (item_x + 30, item_y + 25)) #Drawing text of number of items
            if index_counter < len(inventory_dict):
                index_counter += 1

    index_counter = 0

    spawn_cycle = random.randint(0, fps * 10) #If spawn_cycle == 1(probability = once in 10 seconds) and trees and rocks are < 25, new tree and rock objects will be created
    
    pygame.display.update()
    clock.tick(fps)