import pygame
import random

pygame.font.init()
player_font = pygame.font.SysFont("Calibri", 20)
bot_font = pygame.font.SysFont("Calibri", 15)

time_survived = 0
tot_terr = 10000
width, height = 1000, 700
fps = 100
counter = 0
clock = pygame.time.Clock()
key_cooldown = 0
bots = []
entities = []

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("strategy game")

class Player:
    bluebar_y_val = 300
    territory_flag = False

    def __init__(self, ID):
        self.ID = ID
        self.army = 0
        self.territory = 1000
        self.interest = None           

    def handle_interest(self):
        self.interest = round(self.territory/time_survived)
        self.army += round(self.interest)

    def draw(self):
        self.player_stats = player_font.render(f"Your stats :- Army : {self.army}; Territory  : {self.territory}; Interest : {self.interest}; Time survived : {round(time_survived)}", 1, (255, 255, 255))
        win.blit(self.player_stats, (width/2 - self.player_stats.get_width()/2, height/2 - self.player_stats.get_height()/2))

    def expand(self, per):
        army_per = round(self.army*per/100)
        while available_terr - army_per < 0:
            army_per -= 1
        self.territory += army_per
        self.army -= army_per

    def attack(self, enemy, per):
        army_per = round(self.army*per/100)
        while enemy.territory - army_per/2 < 0:
            army_per -= 1
        enemy.territory -= army_per/2
        self.army -= army_per

    def draw_per_bar(self):
        redbarRect = pygame.Rect(840, 300, 20, 100)
        bluebarRect = pygame.Rect(840, self.bluebar_y_val, 20, 5)
        if pygame.mouse.get_pos()[0] >= 840 and pygame.mouse.get_pos()[0] <= 860 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 400 and pygame.mouse.get_pressed(num_buttons = 3):
            bluebarRect = pygame.Rect(840, pygame.mouse.get_pos()[1], 20, 5)
            self.bluebar_y_val = pygame.mouse.get_pos()[1]
        pygame.draw.rect(win, (255, 0, 0), (redbarRect))
        pygame.draw.rect(win, (0, 0, 255), (bluebarRect))

class Bot(Player):
    def draw(self):
        self.bot_stats = bot_font.render(f"Bot {self.ID}'s stats :- Army : {self.army}; Territory  : {self.territory}; Interest : {self.interest}; Time survived : {round(time_survived)}", 1, (255, 255, 255))
        win.blit(self.bot_stats, (width/2 - self.bot_stats.get_width()/2, height/2 + player.player_stats.get_height()/2 + self.ID*50))

    def attack(self):
        #Randomly selecting an entity to attack
        enemy_ID = self.ID
        while enemy_ID != self.ID:
            enemy_ID = random.randint(0, len(entities) + 1)
        for entity in entities:
            if entity.ID == enemy_ID:
                enemy = entity
        #Calculating the percentage of army to attack
        if self.army < enemy.army:
            per = random.randint(1, 21)
        elif self.army > enemy.army:
            per = random.randint(21, 71)
        elif self.army == enemy.army:
            per = random.randint(10, 31)
        #Attacking
        army_per = round(self.army*per/100)
        while enemy.territory - army_per/2 < 0:
            army_per -= 1
        enemy.territory -= army_per/2
        self.army -= army_per



player = Player(0)
entities.append(player)
for i in range(1, 6):
    bot = Bot(i)
    bots.append(bot)
    entities.append(bot)



running = True
while running:

    clock.tick(fps)

    counter += 1
    var = counter / fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                player.expand(50)
            if event.key == pygame.K_a:
                player.attack(random.choice(bots), 50)

    if var % 1 == 0:  #is similar to time.delay(1) so that the whole program doesn't have to wait 1 second
        time_survived += 1
        player.handle_interest()
        for bot in bots:
            if bot.territory == 0:
                bots.remove(bot)
            else:
                bot.handle_interest()
                choice = random.randint(1, 2)
                if choice == 1:
                    bot.attack()
    
    bots_terr = 0
    for bot in bots:
        bots_terr += bot.territory
    available_terr = tot_terr - (player.territory + bots_terr)

    win.fill((0, 0, 0))
    player.draw()
    for bot in bots:
        bot.draw()

    pygame.display.update()