# -*- coding: utf-8 -*-
import pygame.display

from code import entity
from code.EntityFactory import EntityFactory
from code.entity import Entity


class Level:
    def __init__(self, window, name, meno_option):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass