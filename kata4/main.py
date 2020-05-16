import pygame 

screen_width = 1280
screen_height = 960

# Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width,screen_height))

while True:
    screen.fill(bg_color)
    pygame.display.flip()
    clock.tick(60)
