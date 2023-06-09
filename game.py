import pygame


def calc_score():
    return pygame.time.get_ticks() // 1000 - start_time

def display_score(score):
    score_surf = game_font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))

    screen.blit(score_surf, score_rect)

def display_menu(score):
    screen.fill((94, 129, 162))
    display_score(score)
    screen.blit(player_stand, player_stand_rect)

    start_txt = game_font.render('Press the spacebar to start!', False, (64, 64, 64))
    start_txt_rect = start_txt.get_rect(center=(400, 350))
    screen.blit(start_txt, start_txt_rect)


# initialize pygame
pygame.init()

# set up game window
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Pixel Runner')
game_font = pygame.font.Font('./font/Pixeltype.ttf', 50)
start_time = 0
score = 0

# set up game clock
clock = pygame.time.Clock()

# background music
# music = pygame.mixer.Sound('./audio/music.wav')
# music.set_volume(0.2)
# music.play(loops=-1)

# load graphics assets
sky_surface = pygame.image.load('./graphics/sky.png').convert()
ground_surface = pygame.image.load('./graphics/ground.png').convert()

# snail enemy
snail_surf = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft=(800, 300))

# player
# game
player_surf = pygame.image.load('./graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(150, 300))
player_gravity = 0
# menu
player_stand = pygame.image.load('./graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center=(400,200))

# event loop
running = True
game_active = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # PLAYER INPUT HANDLING
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    snail_rect.left = 800
                    player_rect.bottom = 300

                    start_time = pygame.time.get_ticks() // 1000
                    game_active = True


    if game_active:
        # render background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # score/title
        score = calc_score()
        display_score(score)
        # screen.blit(score_surf, score_rect)

        # render snail enemy
        snail_rect.x -= 4
        if snail_rect.x < -snail_rect.width: snail_rect.x = 800
        screen.blit(snail_surf, snail_rect)

        # render player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300: player_rect.bottom = 300

        screen.blit(player_surf, player_rect)

        # collision -> game over
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        # menu screen
        display_menu(score)


    pygame.display.update()
    clock.tick(60)