#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_OPTION, COLOR_YELLOW, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Battleground3.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/782885__looplicator__66-bpm-industrial-drum-loop-12590-wav.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(100, "O rei", (0, 240, 0), ((1280/2), 70))
            self.menu_text(100, "mago", (0, 240, 0), ((1280 / 2), 140))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(65, MENU_OPTION[i], COLOR_YELLOW, ((1280 / 2), (430 + 60 * i)))
                else:
                    self.menu_text(65, MENU_OPTION[i], COLOR_WHITE, ((1280 / 2), (430 + 60 * i)))
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return  MENU_OPTION[menu_option]





    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Bungee", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)