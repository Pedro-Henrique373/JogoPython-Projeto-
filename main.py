import pygame
from pygame import event

print('Setup Start')

pygame.init()
window = pygame.display.set_mode(size=(600,480))
print('Setup Start')

print('Loop Start')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()