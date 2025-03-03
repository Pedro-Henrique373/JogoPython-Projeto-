#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Battleground3.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/782885__looplicator__66-bpm-industrial-drum-loop-12590-wav.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(100, "Mago", (0, 240, 0), ((1280/2), 70))
            self.menu_text(100, "rei", (0, 240, 0), ((1280 / 2), 140))

            for i in range(len(MENU_OPTION)):
                self.menu_text(65, MENU_OPTION[i], (254, 255, 255), ((1280 / 2), (430 + 60 * i)))

            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Bungee", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)