import pygame

# initialize pygame
pygame.init()

# set up game window
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

# set up game clock
clock = pygame.time.Clock()

# background music
music = pygame.mixer.Sound('./audio/music.wav')
music.set_volume(0.2)
music.play(loops=-1)

# load graphics assets
sky_surface = pygame.image.load('./graphics/sky.png').convert()
ground_surface = pygame.image.load('./graphics/ground.png').convert()

# snail enemy
snail_surf = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft=(800, 300))

# event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # render background
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # render snail enemy
    snail_rect.x -= 4
    if snail_rect.x < -snail_rect.width: snail_rect.x = 800
    screen.blit(snail_surf, snail_rect)

    pygame.display.update()
    clock.tick(60)