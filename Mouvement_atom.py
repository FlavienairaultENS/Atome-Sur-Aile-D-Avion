import matplotlib.pyplot as plt
import numpy as np
from math import *
from gene import Gene
import pygame
import time
from atome import *#Atome
from aile import Aile


max_x = 1040
max_y = 700

clock = pygame.time.Clock()
clock.tick()

pygame.init()
pygame.display.set_caption("atomes")
screen = pygame.display.set_mode((max_x,max_y))

ch = pygame.image.load("images.png")
ch = pygame.transform.scale(ch, (230,800))



background = pygame.Color("white")
gener_ = Gene()
running = True
list_atomex = []
list_atomey = []

for i in range(0,1000):      
        gener_.spawn_atom()


# xl = np.linspace(0, max_x)
# y = [(A/C**4)*(0.14845*(C**3)*((x+cte)/C)**(-0.5) - 0.126*C**3 - 0.7032*(C**2)*(x+cte) + 0.8535*C*(x+cte)**2 -0.406*(x+cte)**3) for x in xl]
# plt.plot(xl, y)
# plt.show()


while running == True:
    clock.tick()
    dt = clock.get_time()
    screen.fill("white")
    screen.blit(gener_.aile.image, [210,45])

    for atome in gener_.all_atom_:
        atome.move(dt)
        pass

    gener_.all_atom_.draw(screen)
    #time.sleep(0.02)#0.02 normalement
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()