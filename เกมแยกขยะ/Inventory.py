import pygame
from pygame.locals import *
from Config import Config
from GameStatus import GameStatus


class Inventory:
    def __init__(self):
        # self.general_waste = 0
        # self.hazardous_waste = 0
        # self.recycle_waste = 0
        # self.food_waste = 0
        GameStatus.count_trash
        self.text_count_trash = fr'จำนวนขยะทั้งหมด {GameStatus.count_trash}/{GameStatus.max_trash}'

        self.bottle = 0
        self.crisps = 0
        self.food = 0
        self.battery = 0

        self.text_bottle = fr'ขวดน้ำ = {self.bottle}'
        self.text_crisps = fr'ถุงขนม = {self.crisps}'
        self.text_food = fr'อาหาร = {self.food}'
        self.text_battery = fr'ถ่านไฟฉาย = {self.battery}'

        self.font = pygame.font.SysFont('Tahoma', size = 21)

        self.color_text = Config.color("red")

        self.count_trash_surface =  self.font.render(self.text_count_trash, True, self.color_text)

        self.bottle_surface =  self.font.render(self.text_bottle, True, self.color_text)
        self.crisps_surface =  self.font.render(self.text_crisps, True, self.color_text)
        self.food_surface =  self.font.render(self.text_food, True, self.color_text)
        self.battery_surface =  self.font.render(self.text_battery, True, self.color_text)

    def update(self):
        self.text_count_trash = fr'จำนวนขยะทั้งหมด {GameStatus.count_trash}/{GameStatus.max_trash}'

        self.text_bottle = fr'ขวดน้ำ = {self.bottle}'
        self.text_crisps = fr'ถุงขนม = {self.crisps}'
        self.text_food = fr'อาหาร = {self.food}'
        self.text_battery = fr'ถ่านไฟฉาย = {self.battery}'

        self.font = pygame.font.SysFont('Tahoma', size = 21)

        self.count_trash_surface =  self.font.render(self.text_count_trash, True, self.color_text)

        self.bottle_surface =  self.font.render(self.text_bottle, True, self.color_text)
        self.crisps_surface =  self.font.render(self.text_crisps, True, self.color_text)
        self.food_surface =  self.font.render(self.text_food, True, self.color_text)
        self.battery_surface =  self.font.render(self.text_battery, True, self.color_text)

    def draw(self, screen):
        screen.blit(self.count_trash_surface, (570, 100))

        screen.blit(self.bottle_surface, (570, 0))
        screen.blit(self.crisps_surface, (570, 25))
        screen.blit(self.food_surface, (570, 50))
        screen.blit(self.battery_surface, (570, 75))