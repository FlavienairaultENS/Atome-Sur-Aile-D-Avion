import pygame


class Aile:
    c = 250
    m = 1
    p = 125
    def __init__(self) :
       self.image = pygame.image.load("aile.png")
       self.image = pygame.transform.scale(self.image, (675,600))