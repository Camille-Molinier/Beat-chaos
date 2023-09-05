import pygame
from world import World

pygame.init()

# générer la fenêtre

pygame.display.set_caption("Chaos")
screen = pygame.display.set_mode((1080, 720))

world = World()
world.run()
