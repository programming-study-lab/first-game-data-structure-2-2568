import pygame
from pygame.locals import *
from Config import Config
import random
from GameStatus import GameStatus

# img_path = 'images'
# bomb_img = pygame.image.load(fr'{img_path}\bomb.png')
# diamond_img = pygame.image.load(fr'{img_path}\diamond.png')
# star_img = pygame.image.load(fr'{img_path}\star.png')
# objects = [bomb_img, star_img, diamond_img]

class Object(pygame.sprite.Sprite):
    def __init__(self, path_object, object_type = '', score = 0):
        super(Object, self).__init__()
        # self.components = []
        # for c in components:
        #     self.add(c)

        self.image = pygame.image.load(fr'{Config.image_path}\{path_object}')
        # self.image.set_colorkey((0, 0, 0), RLEACCEL)
        # self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.image = pygame.transform.scale(self.image, (30, 30))

        # x = random.randint(1, 23) * 32
        # y = random.randint(1, 17) * 32

        x = random.randint(1, 23) * random.randint(7, 32)
        y = random.randint(1, 17) * random.randint(7, 32)

        
        self.rect = self.image.get_rect(x = x, y = y)

        self.count = 1

        self.object_type = object_type
        self.score = score

    def update(self):
        self.rect.move_ip(0, 0)

        

