# Arquivo de testes
import RobPy as rp
import numpy as np

a = rp.cria_vetor3([1, 2, 3])
b = rp.cria_vetor3([4, 5, 6])

if __name__ == '__main__':
    print(rp.norma_vetor(a))