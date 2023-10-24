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

# R = rp.matriz_rotacao_y(77)
# r = rp.cria_vetor3([1,4,-3])
# print(R)
# print(r)
# T = rp.cria_operador4(R,r)
# 
# print(T) # TODO: Consertar

po1 = rp.cria_vetor3([1, 0, 0])
vs1 = rp.cria_vetor3([0, 1, 0])
po2 = rp.cria_vetor3([0, 0, 1])
vs2 = rp.cria_vetor3([1, 0, 0])

print(rp.ang_twist_dir_nc_rad(po1, vs1, po2, vs2)*180/np.pi)