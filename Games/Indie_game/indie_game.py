import pygame
import os
import random

pygame.font.init()

#Variables
width, height = 1000, 600
player_vel = 3
bg_x, bg_y = -500, -500
fps = 60
rock_w, rock_h = 50, 50
tree_w, tree_h = 75, 120
rock_list, tree_list = [], []
inventory_dict = {"rock": 0, "wood": 0, "food": 0}
drop_list = []
inventory_state = False
item_counter = 1
clock = pygame.time.Clock()

main_inventory_font = pygame.font.SysFont("calibri", 30)
inventory_font = pygame.font.SysFont("calibri", 25)

#Window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Indie Game")

#Player image
player_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_img.png")) , (25 * 1.5, 136/4 * 1.5))

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

#Removing background of rocks, trees and player
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

#Player object
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = player_img
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.mask = pygame.mask.from_surface(self.img)
    def draw(self):
        win.blit(self.img, (self.x, self.y))
        self.Rect = pygame.Rect(self.x, self.y, self.w, self.h)

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

#Creating player and rock objects
player = Player(width/2, height/2)
for i in range(25):
        rock = Rock()
        tree = Tree()
        rock_list.append(rock)
        tree_list.append(tree)

#Main loop
running = True
while running:

    clock.tick(fps)

    #Quitting the game if cross button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Filling window with black color
    win.fill((200, 200, 200))
    
    #Detecting movement
    keys = pygame.key.get_pressed()
    if inventory_state == False:
        if keys[pygame.K_a] and player.x - player.h > bg_x:
            bg_x += player_vel
        if keys[pygame.K_d] and player.x + player.h < bg_x + bg_img.get_width():
            bg_x -= player_vel
        if keys[pygame.K_w] and player.y - player.h > bg_y:
            bg_y += player_vel
        if keys[pygame.K_s] and player.y + player.h < bg_y + bg_img.get_height():
            bg_y -= player_vel
        if keys[pygame.K_LCTRL]:
            player_vel = 6
        else:
            player_vel = 3

    if keys[pygame.K_e]:
        inventory_state = True
    if keys[pygame.K_ESCAPE]:
        inventory_state = False
    
    #Drawing background
    win.blit(bg_img, (bg_x, bg_y))

    mouse_pos = pygame.mouse.get_pos()

    #Drawing player, rocks and trees
    for rock in rock_list:
        rock.draw()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos[0] > rock.Rect.x and mouse_pos[0] < rock.Rect.x + rock.Rect.w and mouse_pos[1] > rock.Rect.y and mouse_pos[1] < rock.Rect.y + rock.Rect.h:
                if get_distance(player.x + player.w/2, player.y + player.h/2, rock.Rect.x + rock.w/2, rock.Rect.y + rock.h/2) < 75:
                    rock.strength -= 1
        if rock.strength == 0:
            for i in range(rock.drops):
                drop = Drop(rock.x, rock.y + i*5, rock.h, "rock")
                drop_list.append(drop)
            rock_list.remove(rock)

    for tree in tree_list:
        tree.draw()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos[0] > tree.Rect.x and mouse_pos[0] < tree.Rect.x + tree.Rect.w and mouse_pos[1] > tree.Rect.y and mouse_pos[1] < tree.Rect.y + tree.Rect.h:
                if get_distance(player.x + player.w/2, player.y + player.h/2, tree.Rect.x + tree.w/2, tree.Rect.y + tree.h*3/4) < 50:
                    tree.strength -= 1
        if tree.strength == 0:
            for i in range(tree.drops):
                drop = Drop(tree.x, tree.y + i*10, tree.h, "wood")
                drop_list.append(drop)
            tree_list.remove(tree)

    for drops in drop_list:
        drops.draw()
        if get_distance(player.x + player.w/2, player.y + player.h/2, drops.x + drops.w/2 + bg_x, drops.y + drops.h/2 + bg_y) < 20:
            if drop.type == "wood":
                inventory_dict["wood"] += 1
            elif drop.type == "rock":
                inventory_dict["rock"] += 1
            drop_list.remove(drops)
    
    player.draw()

    if inventory_state:
        inventory_Rect = pygame.Rect(100, 100, width - 200, height - 200)
        pygame.draw.rect(win, (0, 255, 0), inventory_Rect)
        for item in inventory_dict:
            item_text = inventory_font.render(item + ":" + str(inventory_dict[item]), 1, (0, 0, 0))
            win.blit(item_text, (inventory_Rect.x + 10, inventory_Rect.y + 50 + item_counter * 25))
            if item_counter < len(inventory_dict):
                item_counter += 1
        item_counter = 0

        main_inventory_text = main_inventory_font.render("INVENTORY", 1, (0, 0, 0))
        win.blit(main_inventory_text, (inventory_Rect.x + inventory_Rect.w/2 - main_inventory_text.get_width()/2, inventory_Rect.y + 10))

    pygame.display.update()