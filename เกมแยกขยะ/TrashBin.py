import pygame
from pygame.locals import *
from Config import Config
import random
from Text import Text
from Inventory import Inventory
from GameStatus import GameStatus

class TrashBin(pygame.sprite.Sprite):
    def __init__(self, path_object, object_type = '', x = 0, y = 0):
        super(TrashBin, self).__init__()
        self.image = pygame.image.load(fr'{Config.image_path}\{path_object}')

        self.image = pygame.transform.scale(self.image, (30, 30))

        # x = random.randint(1, 22) * 32
        # y = random.randint(1, 16) * 32

        x = random.randint(1, 23) * random.randint(7, 32)
        y = random.randint(1, 17) * random.randint(7, 32)

        self.rect = self.image.get_rect(x = x, y = y)

        self.count = 0
        self.object_type = object_type
        self.score = 0


    def update(self, screen, player, inventory, trash_bin_group, keys):

        delay = Config.delay_button_drop_item
        # pygame.time.wait(delay) = pygame.time.wait(delay)
        
        hits = pygame.sprite.spritecollide(
            player, trash_bin_group, False, pygame.sprite.collide_circle
        )

        if len(hits) > 0:
            for hit in hits:
                first_hit = hit
                break
           

            if GameStatus.count_trash != GameStatus.max_trash and GameStatus.game_over == False:

                if inventory.bottle != 0 or \
                    inventory.crisps != 0 or \
                    inventory.food != 0 or \
                    inventory.battery != 0:
                     
                    if first_hit.object_type == 'trash-bin-blue':

                        if keys[pygame.K_1]: # ขวดน้ำ สีเหลือง
                            if inventory.bottle != 0:
                                first_hit.count += 1
                                first_hit.score -= 3
                                inventory.bottle -= 1
                                GameStatus.total_score -= 3
                                GameStatus.yellow_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)

                        elif keys[pygame.K_2]: # ขนม สีน้ำเงิน
                            if inventory.crisps != 0:
                                first_hit.count += 1
                                first_hit.score += 1
                                inventory.crisps -= 1
                                GameStatus.total_score += 1
                                GameStatus.blue_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_3]: # อาหาร สีเขียว
                            if inventory.food != 0:
                                first_hit.count += 1
                                first_hit.score -= 2
                                inventory.food -= 1
                                GameStatus.total_score -= 2
                                GameStatus.green_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_4]: # ถ่านไฟฉาย สีแดง
                            if inventory.battery != 0:
                                first_hit.count += 1
                                first_hit.score -= 5
                                inventory.battery -= 1
                                GameStatus.total_score -= 5
                                GameStatus.red_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)

                    elif first_hit.object_type == 'trash-bin-green':
                        if keys[pygame.K_1]: # ขวดน้ำ สีเหลือง
                            if inventory.bottle != 0:
                                first_hit.count += 1
                                first_hit.score -= 3
                                inventory.bottle -= 1
                                GameStatus.total_score -= 3
                                GameStatus.yellow_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_2]: # ขนม สีน้ำเงิน
                            if inventory.crisps != 0:
                                first_hit.count += 1
                                first_hit.score -= 1
                                inventory.crisps -= 1
                                GameStatus.total_score -= 1
                                GameStatus.blue_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_3]: # อาหาร สีเขียว
                            if inventory.food != 0:
                                first_hit.count += 1
                                first_hit.score += 2
                                inventory.food -= 1
                                GameStatus.total_score += 2
                                GameStatus.green_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_4]: # ถ่านไฟฉาย สีแดง
                            if inventory.battery != 0:
                                first_hit.count += 1
                                first_hit.score -= 5
                                inventory.battery -= 1
                                GameStatus.total_score -= 5
                                GameStatus.red_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)

                    elif first_hit.object_type == 'trash-bin-yellow':
                        if keys[pygame.K_1]: # ขวดน้ำ สีเหลือง
                            if inventory.bottle != 0:
                                first_hit.count += 1
                                first_hit.score += 3
                                inventory.bottle -= 1
                                GameStatus.total_score += 3
                                GameStatus.yellow_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_2]: # ขนม สีน้ำเงิน
                            if inventory.crisps != 0:
                                first_hit.count += 1
                                first_hit.score -= 1
                                inventory.crisps -= 1
                                GameStatus.total_score -= 1
                                GameStatus.blue_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_3]: # อาหาร สีเขียว
                            if inventory.food != 0:
                                first_hit.count += 1
                                first_hit.score -= 2
                                inventory.food -= 1
                                GameStatus.total_score -= 2
                                GameStatus.green_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_4]: # ถ่านไฟฉาย สีแดง
                            if inventory.battery != 0:
                                first_hit.count += 1
                                first_hit.score -= 5
                                inventory.battery -= 1
                                GameStatus.total_score -= 5
                                GameStatus.red_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)

                    elif first_hit.object_type == 'trash-bin-red':
                        if keys[pygame.K_1]: # ขวดน้ำ สีเหลือง
                            if inventory.bottle != 0:
                                first_hit.count += 1
                                first_hit.score -= 3
                                inventory.bottle -= 1
                                GameStatus.total_score -= 3
                                GameStatus.yellow_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_2]: # ขนม สีน้ำเงิน
                            if inventory.crisps != 0:
                                first_hit.count += 1
                                first_hit.score -= 1
                                inventory.crisps -= 1
                                GameStatus.total_score -= 1
                                GameStatus.blue_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_3]: # อาหาร สีเขียว
                            if inventory.food != 0:
                                first_hit.count += 1
                                first_hit.score -= 2
                                inventory.food -= 1
                                GameStatus.total_score -= 2
                                GameStatus.green_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                        elif keys[pygame.K_4]: # ถ่านไฟฉาย สีแดง
                            if inventory.battery != 0:
                                first_hit.count += 1
                                first_hit.score += 5
                                inventory.battery -= 1
                                GameStatus.total_score += 5
                                GameStatus.red_trash_bin_score = first_hit.score

                                GameStatus.count_trash += 1
                                pygame.time.delay(delay)
                                # pygame.time.wait(delay)
                    
                    # print("ccccccccccccccccccc: ", first_hit.score)
            
                    # print(fr'trash_bin_{self.object_type}')

            if GameStatus.count_trash == GameStatus.max_trash:
                # print("end game")
                # GameStatus.running = False
                GameStatus.game_over = True
                # GameStatus.playing = False
                GameStatus.win = True


            Text.draw(screen, 'กดปุ่มตัวเลข เพื่อวางสิ่งของ', 21, 10, 0, 'green')
            Text.draw(screen, 'ปุ่ม 1 ทิ้งขวดน้ำ', 21, 20, 25, 'green')
            Text.draw(screen, 'ปุ่ม 2 ทิ้งถุงขนม', 21,20, 50, 'green')
            Text.draw(screen, 'ปุ่ม 3 ทิ้งเศษอาหาร', 21, 20, 75, 'green')
            Text.draw(screen, 'ปุ่ม 4 ทิ้งถ่านไฟฉาย', 21, 20, 100, 'green')
            
            # print("total_score: ", GameStatus.total_score)
            # print("GameStatus.count_trash: ", GameStatus.count_trash, " / ", GameStatus.max_trash)

                

        


