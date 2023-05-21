import pygame

# initialize pygame
pygame.init()

# set up game window
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

# event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False