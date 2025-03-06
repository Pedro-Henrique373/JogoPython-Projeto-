import pygame
from pygame import event
from code.menu import Menu
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(1280, 710))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass