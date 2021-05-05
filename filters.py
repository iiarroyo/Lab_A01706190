import numpy as np
'''
Filters.py
lista de kernels/filtros a usar
'''

gaussian_blur = np.array([
    [0,0,0,5,0,0,0],
    [0,5,18,32,18,5,0],
    [0,18,64,100,64,18,0],
    [5,32,100,100,100,32,5],
    [0,18,64,100,64,18,0],
    [0,5,18,32,18,5,0],
    [0,0,0,5,0,0,0]])

edge_detection = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
