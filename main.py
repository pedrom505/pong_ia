from Window import Screen
import pygame
import time

running = True
screen = Screen((800, 800))
screen.icon("icon.png")
screen.caption("Pong_IA")

surface = screen.get_surface()

x = 100
y = 100

dt = 0
count = 0
while running:
    time1 = time.time()
    clock = pygame.time.Clock()

    key = pygame.key.get_pressed()

    if key[pygame.K_UP]:
        y -= 1
    if key[pygame.K_DOWN]:
        y += 1
    if key[pygame.K_LEFT]:
        x -= 1
    if key[pygame.K_RIGHT]:
        x += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.background(image_name="background.jpg")

    pygame.draw.circle(surface, (0, 0, 255), (x, y), 75)

    print(clock.get_fps())

    screen.update()

screen.close()