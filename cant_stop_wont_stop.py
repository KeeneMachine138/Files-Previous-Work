import pygame

# Initiate Pygame
pygame.init()

# Making the window/screen
window_screen = pygame.display.set_mode((500,500))

# Displaying the Game's name/title
pygame.display.set_caption("Couldn't stop with just 1")

# Player Characteristics

# Player x-axis starting position
x = 50
# Player y-axis starting position
y = 50
# Player's width
width = 40
# Player's height
height = 60
# The speed at which the player moves - vel = velocity
vel = 5

#

# Game Loop - The Main Loop
run = True
while run:

    # pygame.time.delay - Controls and delays the speed of how fast things move in Game Loop
    pygame.time.delay(100)

    # Allows us to quit app easier
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width:
        x = x + vel
    if not(is_jump): 
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < screen_length:
            y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            negative = 1
            if jump_count < 0:
                negative = -1
            y -= (jump_count ** 2) * .5 * negative
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    window_screen.fill((0,0,0))
    pygame.draw.rect(window_screen, (255, 160, 79), (x, y, width, height))
    pygame.display.update()

pygame.quit()
