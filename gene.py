import pygame
from atome import Atome
from aile import Aile


class Gene:

    def __init__(self) :
        self.mult_atom = pygame.sprite.Group()
        self.atom_ = Atome(1,self)
        self.mult_atom.add(self.atom_)
        self.all_atom_ = pygame.sprite.Group()
        # self.spawn_atom()
        self.aile = Aile()
       

    def spawn_atom(self):
        atome_ = Atome(1,self)
        self.all_atom_.add(atome_)
