# Israel Arroyo
# conv.py
# primera version, tamaño estatico
import numpy as np

image = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]])
filt = np.array([[1,1,1],[0,0,0],[2,10,3]])
filter_col=3
filter_row=3
res = np.zeros([3,4])
for i in range(3): # res_row
    for j in range(4):# res_col
        res[i,j] = np.sum(image[i:i+filter_row,j:j+filter_col]*filt)
print(res)