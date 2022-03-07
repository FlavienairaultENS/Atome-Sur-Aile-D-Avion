
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
from math import *
xmax = 505
x = np.linspace(0,xmax,xmax+1)
A = 500
C = 500
plt.ylim(-200,300)
plt.xlim(-10,xmax+10)
y_sup_aile = 100+(A)*(0.2969*(x/C)**0.5 - 0.126 * x/C - 0.3516*(x/C)**2 + 0.2845*(x/C)**3 -0.1015*(x/C)**4)
y_inf_aile = (-y_sup_aile + 100*2)
plt.fill_between(x,y_sup_aile,100,where = (x > 0) & (x <= xmax),color='0.8')
plt.fill_between(x,100,y_inf_aile,where = (x > 0) & (x <= xmax),color='0.8')
plt.plot(x,y_sup_aile,color = 'black')
plt.plot(x, y_inf_aile,color = 'black')
plt.show()
