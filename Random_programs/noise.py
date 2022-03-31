import pygame

width, height = 500, 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Noise")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))
    pygame.display.update()