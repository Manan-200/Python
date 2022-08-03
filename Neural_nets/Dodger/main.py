import neat
import pygame
import random
import os

width, height = 900, 700
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 120

class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 20
        self.h = 20
    def draw(self):
        self.Rect = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        pygame.draw.rect(win, (0, 0, 255), self.Rect)

class Meteor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 10
        self.h = 10
    def draw(self):
        self.Rect = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        pygame.draw.rect(win, (255, 0, 0), self.Rect)

def main(genomes, config):
    nets = []
    ge = []
    ships = []
    meteors = []
    x_meteors = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        ships.append(Ship(width/2, 9*height/10))
        g.fitness = 0
        ge.append(g)

    score = 0

    #MAIN LOOP
    run = True
    while run:

        clock.tick(fps)
        win.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

        #Adding meteors
        while len(meteors) < 150:
            meteor = Meteor(random.randint(0, width), random.randint(-5000, -1500))
            meteors.append(meteor)

        for x, ship in enumerate(ships):
            ship.draw()
            ge[x].fitness += 0.1
            for meteor in meteors:
                if abs(ship.x - meteor.x) <= 25 and meteor.y > 0:
                    x_meteors.append(meteor)
            for meteor in x_meteors:
                output = nets[x].activate((ship.x, meteor.x - 25, meteor.x + 25))
                if output[0] > 0:
                    ship.x -= 3
                if output[0] < 0:
                    ship.x += 3
            x_meteors.clear()

        #Handling meteors
        for meteor in meteors:
            meteor.y += 5
            meteor.draw()
            if meteor.y > height:
                meteors.remove(meteor)
            for x, ship in enumerate(ships):
                if ship.Rect.colliderect(meteor.Rect) or ship.x <= 0 or ship.x >= width:
                    ge[x].fitness -= 1
                    ships.pop(x)
                    nets.pop(x)
                    ge.pop(x)

        pygame.display.update()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation, 
                            config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path)