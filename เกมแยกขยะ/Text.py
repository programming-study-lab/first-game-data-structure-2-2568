import pygame
from pygame.locals import *
from Config import Config

class Text:
    def __init__(self):
        pass

    def draw(screen, text, size, x, y, color_name = ''):

        if color_name == '':
            color_name = 'black'

        font = pygame.font.SysFont('Tahoma', size)
        text_surface = font.render(text, True, Config.color(color_name))
        # text_rect = text_surface.get_rect(midtop=(x, y))
        screen.blit(text_surface, (x, y))