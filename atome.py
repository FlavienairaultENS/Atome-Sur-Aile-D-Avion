import pygame
import random
import numpy as np

max_x = 1040
max_y = 700
C = 500
A = 500
cte = -300
y_sup_aile = 0
y_inf_aile = 0
offset_x = 300

def calcY(x):
        return offset_x + A*(0.2969*((x+cte)/C)**0.5 - 0.126 * (x+cte)/C - 0.3516*((x+cte)/C)**2 + 0.2845*((x+cte)/C)**3 -0.1015*((x+cte)/C)**4)

startAile = calcY(-cte)
print(startAile)


class Atome(pygame.sprite.Sprite):

    
    def __init__(self,v, col):
        super().__init__()
        self.col = col
        self.vitesse = v
        self.r = 3
        # self.image = pygame.image.load("atome.png")
        # self.image = pygame.transform.scale(self.image, (17,17))


        self.posx, self.posy = self.genRandPos()
        # y_sup_aile = offset_x + A*(0.2969*((self.posx+cte)/C)**0.5 - 0.126 * (self.posx+cte)/C - 0.3516*((self.posx+cte)/C)**2 + 0.2845*((self.posx+cte)/C)**3 -0.1015*((self.posx+cte)/C)**4)
        # y_inf_aile = (-y_sup_aile + offset_x*2)
        
        if self.isInside(self.posx, self.posy):
            nx, ny = self.genRandPos()
            while self.isInside(nx, ny):
                ny, ny = self.genRandPos()
            self.posx, self.posy = nx, ny


        self.image = pygame.Surface((self.r*2, self.r*2), pygame.SRCALPHA)
        self.image.fill(pygame.Color(0,0,0,0))
        pygame.draw.circle(self.image, pygame.Color(0,0,0), (self.r, self.r), self.r)

        self.rect = self.image.get_rect()
        self.rect.x = self.posx
        self.rect.y = self.posy                  
        self.vit_init_x = random.randint(1,10)*random.choice([-1,1])/70
        self.vit_init_y = random.randint(1,10)*random.choice([-1,1])/70

    def move(self, dt):

        # y_sup_aile = 0
        # y_inf_aile = 0
        # if self.posx > -cte and self.posx < C - cte:
        #     y_sup_aile = offset_x + A*(0.2969*((self.posx+cte)/C)**0.5 - 0.126 * (self.posx+cte)/C - 0.3516*((self.posx+cte)/C)**2 + 0.2845*((self.posx+cte)/C)**3 -0.1015*((self.posx+cte)/C)**4)
        #     y_inf_aile = (-y_sup_aile + offset_x*2)
            
        # if self.posx <= 0 or self.posx >= max_x :
        #     self.vit_init_x = -self.vit_init_x
                 
        # if self.posy <= 0 or self.posy >= max_y:
        #     self.vit_init_y = -self.vit_init_y 
        
        # if  (self.posy < y_sup_aile and self.posx <C-cte and  self.posy > y_inf_aile and self.posx>-cte):
 
        #     # if (self.init == 1):
        #     #     self.vit_init_x = - self.vit_init_x
        #     #     self.vit_init_y = - self.vit_init_y
        #     #     self.posx += self.vit_init_x * dt
        #     #     self.posy += self.vit_init_y * dt
        #     #     self.init = 0
        #     #     print("etat initial")
        #     # else:
        #         y_sup_aile_prime = (A/C**4)*(0.14845*(C**3)*((self.posx+cte)/C)**(-0.5) - 0.126*C**3 - 0.7032*(C**2)*(self.posx+cte) + 0.8535*C*(self.posx+cte)**2 -0.406*(self.posx+cte)**3)
        #         y_inf_aile_prime = -y_sup_aile_prime
        #         if self.posy >= offset_x:
        #             tangante2 = y_inf_aile_prime*(10000-self.posx)+y_inf_aile
        #             beta = np.arctan((tangante2 - y_inf_aile)/(10000 - self.posx))
        #         else:
        #             tangante2 = y_sup_aile_prime*(10000-self.posx)+y_sup_aile
        #             beta = np.arctan((tangante2 - y_inf_aile)/(10000 - self.posx))
        #         # print(beta)
        #         self.vit_init_x = - self.vit_init_x
        #         self.vit_init_y = - self.vit_init_y


        nextx = self.posx + self.vit_init_x * dt
        nexty = self.posy + self.vit_init_y * dt


        if nextx <= 0 or nextx >= max_x :
            self.vit_init_x = -self.vit_init_x
                 
        if nexty <= 0 or nexty >= max_y:
            self.vit_init_y = -self.vit_init_y 

        if self.isInside(nextx, nexty):

            tx = 1
            if cte + self.posx > 0:
                ty = A*(-0.126 * C**3 - 0.7032*C**2 * (cte + self.posx) + 0.8535 * C * (cte + self.posx)**2 - 0.406 * (cte + self.posx)**3 + (0.14845* C**3)/((cte + self.posx)/C)**0.5)/C**4
                ty = -ty if self.posy < startAile else ty
            else:
                ty = 1
                tx = 0
                print(self.posx)
            l = np.sqrt(tx**2 + ty**2)
            tx, ty = tx/l, ty/l


            scal = self.vit_init_x * tx + self.vit_init_y * ty


            self.vit_init_x = -self.vit_init_x + 2 * tx * scal
            self.vit_init_y = -self.vit_init_y + 2 * ty * scal




            nextx = self.posx
            nexty = self.posy



        self.posx = nextx
        self.posy = nexty

        self.rect.x = int(self.posx)
        self.rect.y = int(self.posy)

    def isInside(self,x,y):
        if x < -cte and x > C - cte:
            return False
        y_sup_aile = calcY(x)
        y_inf_aile = (-y_sup_aile + offset_x*2)
        if isinstance(y_sup_aile, complex):
            return False
        return y_inf_aile < y < y_sup_aile

    def genRandPos(self):
        return (random.randint(1,max_x), random.randint(1,max_y))
