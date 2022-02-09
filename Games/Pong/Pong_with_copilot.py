#Make pong in pygame

import pygame

width, height = 640, 480
vel = 5
x_vel, y_vel = 1, 1
fps = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

player1Rect = pygame.Rect(10, height/2 - 50, 20, 100)
player2Rect = pygame.Rect(width - 30, height/2 - 50, 20, 100)
ballRect = pygame.Rect(width // 2 - 10, height // 2 - 10, 20, 20)

#Loop
running = True
while running:

    clock.tick(fps)

    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1Rect.y -= vel
    if keys[pygame.K_s]:
        player1Rect.y += vel
    if keys[pygame.K_UP]:
        player2Rect.y -= vel
    if keys[pygame.K_DOWN]:
        player2Rect.y += vel

    #Checking for offscreen
    if player1Rect.y < 0:
        player1Rect.y = 0
    if player1Rect.y > height - player1Rect.height:
        player1Rect.y = height - player1Rect.height
    if player2Rect.y < 0:
        player2Rect.y = 0
    if player2Rect.y > height - player2Rect.height:
        player2Rect.y = height - player2Rect.height

    #Moving ball
    ballRect.x += x_vel
    ballRect.y += y_vel

    #Checking for collisions
    if ballRect.colliderect(player1Rect):
        x_vel = -x_vel
    if ballRect.colliderect(player2Rect):
        x_vel = -x_vel
    if ballRect.x < 0:
        print("Player 2 wins!")
        running = False
    if ballRect.x > width:
        print("Player 1 wins!")
        running = False
    if ballRect.y < 0:
        y_vel = -y_vel
    if ballRect.y + 20 > height:
        y_vel = -y_vel

    #Draw
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), player1Rect)
    pygame.draw.rect(screen, (255,255,255), player2Rect)
    pygame.draw.rect(screen, (255,255,255), ballRect)
    pygame.display.flip()