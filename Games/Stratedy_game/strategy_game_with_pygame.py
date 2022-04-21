import pygame

pygame.font.init()
player_font = pygame.font.SysFont("Calibri", 20)
bot_font = pygame.font.SysFont("Calibri", 15)

time_survived = 0
available_territory = 10000
width, height = 1000, 700
fps = 100
counter = 0
clock = pygame.time.Clock()
key_cooldown = 0
bots = []

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("strategy game")

class Player:
    bluebar_y_val = 300
    territory_flag = False

    def __init__(self, ID):
        self.id = ID
        self.army = 0
        self.territory = 1000
        self.interest = None           

    def handle_interest(self):
        self.interest = round(self.territory/time_survived)
        self.army += round(self.interest)

    def draw(self):
        self.player_stats = player_font.render(f"Your stats :- Army : {self.army}; Territory  : {self.territory}; Interest : {self.interest}; Time survived : {round(time_survived)}", 1, (255, 255, 255))
        win.blit(self.player_stats, (width/2 - self.player_stats.get_width()/2, height/2 - self.player_stats.get_height()/2))

    def expand(self, percent):
        global available_territory
        army_per = round(self.army*percent/100)
        while available_territory - army_per < 0:
            army_per -= 1
        self.territory += army_per
        self.army -= army_per
        #bot_1.army -= 10
        available_territory -= army_per


    def draw_percent_bar(self):
        redbarRect = pygame.Rect(840, 300, 20, 100)
        bluebarRect = pygame.Rect(840, self.bluebar_y_val, 20, 5)
        if pygame.mouse.get_pos()[0] >= 840 and pygame.mouse.get_pos()[0] <= 860 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 400 and pygame.mouse.get_pressed(num_buttons = 3):
            bluebarRect = pygame.Rect(840, pygame.mouse.get_pos()[1], 20, 5)
            self.bluebar_y_val = pygame.mouse.get_pos()[1]
        pygame.draw.rect(win, (255, 0, 0), (redbarRect))
        pygame.draw.rect(win, (0, 0, 255), (bluebarRect))

class Bot(Player):
    def draw(self):
        self.bot_stats = bot_font.render(f"Bot {self.id}'s stats :- Army : {self.army}; Territory  : {self.territory}; Interest : {self.interest}; Time survived : {round(time_survived)}", 1, (255, 255, 255))
        win.blit(self.bot_stats, (width/2 - self.bot_stats.get_width()/2, height/2 + player.player_stats.get_height()/2 + self.id*50))

            
player = Player(0)
for i in range(1, 6):
    bot = Bot(i)
    bots.append(bot)

while True:

    clock.tick(fps)

    counter += 1
    var = counter / fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_e] and key_cooldown <= var:
        key_cooldown += 1
        player.expand(50)

    if var % 1 == 0:  #is similar to time.delay(1) so that the whole program doesn't have to wait 1 second 
        time_survived += 1
        player.handle_interest()
        for bot in bots:
            bot.handle_interest()

    win.fill((0, 0, 0))
    player.draw()
    for bot in bots:
        bot.draw()
    #player.draw_percent_bar()

    pygame.display.update()