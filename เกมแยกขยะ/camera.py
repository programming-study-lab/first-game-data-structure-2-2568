import pygame

camera = pygame.Rect(0, 0, 0, 0)


def create_screen(width, height, tile):
    pygame.display.set_caption(tile)

    screen = pygame.display.set_mode((width, height))


    camera.width = width
    camera.height = height

    return screen