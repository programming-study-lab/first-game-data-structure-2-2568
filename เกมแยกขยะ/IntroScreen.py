import pygame, sys
from pygame.locals import *
from Text import Text
from Config import Config


class IntroScreen:
    def __init__(self, screen):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

    def draw(self):
        self.screen.fill(Config.color('black'))

        image_start_game = pygame.image.load(fr'{Config.image_path}\images2\image-start-game.png')
        self.screen.blit(image_start_game, self.screen.get_rect())

        Text.draw(self.screen, "เกมแยกขยะ", 72, 250, 30, 'white')
        Text.draw(self.screen, "แยกประเภทขยะทั้งสี่ประเภทให้ถูกต้อง", 24, 225, 200, 'white')

        #แสดงปุ่ม EXIT
        btn_exit_image = pygame.image.load(fr'{Config.image_path}\images2\btn-exit.png')
        btn_exit_rect = btn_exit_image.get_rect(
            right=self.screen_rect.centerx - 50, top=320
        )   

        #แสดงปุ่ม START
        btn_start_image = pygame.image.load(fr'{Config.image_path}\images2\btn-start.png')
        btn_start_rect = btn_start_image.get_rect(
            left = self.screen_rect.centerx + 50, top=320
        )

        self.screen.blit(btn_start_image, btn_start_rect)
        self.screen.blit(btn_exit_image, btn_exit_rect)

        pygame.display.flip()

        waiting = True
        while waiting:
            
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    # start game
                    if btn_start_rect.collidepoint(pygame.mouse.get_pos()):
                        waiting = False
                    # exit game
                    elif btn_exit_rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                elif keys[K_g]:
                    waiting = False

        


        

