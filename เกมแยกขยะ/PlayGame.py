
import sys, pygame
from pygame.locals import *
from map import TileKind, Map




from Player import Player
from camera import create_screen
# from Entity import Entity, active_objs
# from Sprite import sprites, Sprite
# import random
# from physics import Body
from Object import Object
from Inventory import Inventory
from TrashBin import TrashBin
# from Button import Button
from GameStatus import GameStatus
from Config import Config
from IntroScreen import IntroScreen
from Text import Text



# SCREEN_W = 800
# SCREEN_H = 600
# FPS = 30
clock = pygame.time.Clock()

pygame.init()
# pygame.display.set_caption("pyGame")

screen = create_screen(Config.SCREEN_W, Config.SCREEN_H, Config.GAME_NAME)
screen_rect = screen.get_rect()

keys = pygame.key.get_pressed()


tile_kinds = [
    TileKind("dirt", "images/dirt.png", False),
    TileKind("grass", "images/grass.png", False),
    TileKind("water", "images/water.png", True),
    TileKind("wood", "images/wood.png", False),
]


map = Map("maps/start.map", tile_kinds, 32)


while GameStatus.running:

    if not GameStatus.playing or GameStatus.restart:

        if not GameStatus.restart:
            introScreen = IntroScreen(screen)
            introScreen.draw()

        GameStatus.playing = True
        GameStatus.restart = False

        GameStatus.game_over = False
        GameStatus.total_score = 0
        GameStatus.win = False
        GameStatus.lose = False
        GameStatus.total_score = 0
        GameStatus.blue_trash_bin_score = 0
        GameStatus.green_trash_bin_score = 0
        GameStatus.yellow_trash_bin_score = 0
        GameStatus.red_trash_bin_score = 0
        GameStatus.count_trash = 0

        player = Player(screen_rect)
        inventory = Inventory()


        food_group = pygame.sprite.Group()
        for i in range(GameStatus.food_trash):
            food_group.add(Object('images2/fish.png', object_type = 'food', score = 10))

        crisps_group = pygame.sprite.Group()
        for i in range(GameStatus.crisps_trash):
            crisps_group.add(Object('images2/crisps.png', object_type = 'crisps', score = 10))

        bottle_group = pygame.sprite.Group()
        for i in range(GameStatus.bottle_trash):
            bottle_group.add(Object('images2/bottle.png', object_type = 'bottle', score = 10))

        battery_group = pygame.sprite.Group()
        for i in range(GameStatus.battery_trash):
            battery_group.add(Object('images2/battery.png', object_type = 'battery', score = 10))

        trash_bin_blue = pygame.sprite.Group()
        trash_bin_blue.add(TrashBin('images2/trash-bin-blue.png', 'trash-bin-blue'))

        trash_bin_green = pygame.sprite.Group()
        trash_bin_green.add(TrashBin('images2/trash-bin-green.png', 'trash-bin-green'))

        trash_bin_red = pygame.sprite.Group()
        trash_bin_red.add(TrashBin('images2/trash-bin-red.png', 'trash-bin-red'))

        trash_bin_yellow = pygame.sprite.Group()
        trash_bin_yellow.add(TrashBin('images2/trash-bin-yellow.png', 'trash-bin-yellow'))

        # button_group = pygame.sprite.Group()
        # button_group.add(Button('images2/button-blue2.png', 'button')) 


    for e in pygame.event.get():

        keys = pygame.key.get_pressed()

        if e.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif keys[K_SPACE] and GameStatus.game_over:
            GameStatus.playing = False
        elif keys[K_r]:
            GameStatus.restart = True
        elif keys[K_ESCAPE]:
            GameStatus.playing = False

    # for a in active_objs:
    #     a.update()

    
        
    screen.fill((135, 205, 235))
    map.draw(screen)

    trash_bin_blue.update(screen, player, inventory, trash_bin_blue, keys)
    trash_bin_blue.draw(screen)

    trash_bin_green.update(screen, player, inventory, trash_bin_green, keys)
    trash_bin_green.draw(screen)

    trash_bin_yellow.update(screen, player, inventory, trash_bin_yellow, keys)
    trash_bin_yellow.draw(screen)

    trash_bin_red.update(screen, player, inventory, trash_bin_red, keys)
    trash_bin_red.draw(screen)
    
    player.update(keys)
    player.draw(screen)
    
    # food_group.update()
    food_group.draw(screen)
    
    # crisps_group.update()
    crisps_group.draw(screen)

    # bottle_group.update()
    bottle_group.draw(screen)
    
    # battery_group.update()
    battery_group.draw(screen)


    inventory.update()
    inventory.draw(screen)

    if GameStatus.game_over:
        if GameStatus.win:
            screen.fill(Config.color('blue'))

            image_end_game = pygame.image.load(fr'{Config.image_path}\images2\image-end-game.png')
            screen.blit(image_end_game, screen.get_rect())

            Text.draw(screen, "จบเกม", 55, 150, 100)
            Text.draw(screen, fr"คะแนนรวม = {GameStatus.total_score}/{GameStatus.max_total_score}", 55, 150, 165)
            Text.draw(screen, fr"ถังขยะสีน้ำเงิน = {GameStatus.blue_trash_bin_score}/{GameStatus.max_blue_trash_bin_score}", 55, 150, 230)
            Text.draw(screen, fr"ถังขยะสีเขียว = {GameStatus.green_trash_bin_score}/{GameStatus.max_green_trash_bin_score}", 55, 150, 290)
            Text.draw(screen, fr"ถังขยะสีเหลือง = {GameStatus.yellow_trash_bin_score}/{GameStatus.max_yellow_trash_bin_score}", 55, 150, 360)
            Text.draw(screen, fr"ถังขยะสีแดง = {GameStatus.red_trash_bin_score}/{GameStatus.max_red_trash_bin_score}", 55, 150, 425)
            Text.draw(screen, fr"กดปุ่ม spacebar เพื่อกลับหน้าแรก", 21, 150, 550)
    
    pygame.display.flip()
    clock.tick(Config.FPS)

    hits_food = pygame.sprite.spritecollide(
            player, food_group, True, pygame.sprite.collide_mask
    )

    hits_crisps = pygame.sprite.spritecollide(
            player, crisps_group, True, pygame.sprite.collide_mask
    )

    hits_bottle = pygame.sprite.spritecollide(
            player, bottle_group, True, pygame.sprite.collide_mask
    )

    hits_battery = pygame.sprite.spritecollide(
            player, battery_group, True, pygame.sprite.collide_mask
    )


    if len(hits_food) > 0:
        for hit in hits_food:
            first_hit = hit
            break
        if first_hit.object_type == 'food':
            inventory.food += 1
    
    if len(hits_crisps) > 0:
        for hit in hits_crisps:
            first_hit1 = hit
            break

        if first_hit1.object_type == 'crisps':
            inventory.crisps += 1

    if len(hits_bottle) > 0:
        for hit in hits_bottle:
            first_hit2 = hit
            break
        if first_hit2.object_type == 'bottle':
            inventory.bottle += 1

    if len(hits_battery) > 0:
        for hit in hits_battery:
            first_hit3 = hit
            break
        if first_hit3.object_type == 'battery':
            inventory.battery += 1

print("\n***** End Game *****\n")