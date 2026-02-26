import pygame, sys
from Config import Config
from camera import camera

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_rect):
        # super(Alien, self).__init__()
        self.image = pygame.image.load(fr'{Config.image_path}/player.png')

        # self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (80, 80))
        
        self.rect = self.image.get_rect(
            center = screen_rect.center
        )

        self.speed_move = Config.speed_move
        # self.total_score = 0
    
    def update(self, keys):
        speed_move = self.speed_move

        if keys[pygame.K_w]:
            # print("w")
            self.rect.move_ip(0, -speed_move)
            if self.rect.top < 0:
                self.rect.top = 0
        if keys[pygame.K_a]:
            # print("a")
            self.rect.move_ip(-speed_move, 0)
            if self.rect.left < 0:
                self.rect.left = 0
        if keys[pygame.K_s]:
            # print("s")
            self.rect.move_ip(0, speed_move)
            if self.rect.bottom > Config.SCREEN_H:
                self.rect.bottom = Config.SCREEN_H
        if keys[pygame.K_d]:
            # print("d")
            self.rect.move_ip(speed_move, 0)
            if self.rect.right > Config.SCREEN_W:
                self.rect.right = Config.SCREEN_W
        
        # camera.x = self.rect



    def draw(self, screen):
        screen.blit(self.image, self.rect)