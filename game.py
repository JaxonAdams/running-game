import pygame

# initialize pygame
pygame.init()

# set up game window
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

# set up game clock
clock = pygame.time.Clock()

# load graphics assets
sky_surface = pygame.image.load('./graphics/sky.png').convert()
ground_surface = pygame.image.load('./graphics/ground.png').convert()

# event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    pygame.display.update()
    clock.tick(60)