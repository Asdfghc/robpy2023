# Arquivo de testes
import RobPy as rp
import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

#a = rp.cria_vetor3([1, 2, 3])
#b = rp.cria_vetor3([4, 5, 6])
#
#
#
#fig = plot.figure()
#ax = Axes3D(fig)
#fig.add_axes(ax)
#rp.plota_vetor3(a,color='r')
#rp.plota_vetor3(b,vo=a,color='r')
#plot.xlabel('Eixo X')
#plot.ylabel('Eixo Y')
#ax.set_zlabel('Eixo Z')
#plot.show()

R = rp.matriz_rotacao_y(77)
r = rp.cria_vetor3([1,4,-3])

T = rp.cria_operador4(R,r)

print(T) # TODO: Consertar