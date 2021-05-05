# Israel Arroyo A01706190
# conv.py
# segunda version, funcion que recibe tamaño de imagen variable
import numpy as np

def conv(image, filt, padding_shape = [0,0]):
    '''
    recibe imagen, filtro/kernel y el shape de padding deseado
    devuelve convolucion valida
    '''
    S = 1 # default: no stride
    # default: no padding
    filter_row,filter_col = filt.shape
    image_row,image_col=image.shape
    res_row = int((image_row- filter_row + 2*padding_shape[0])/S +1)
    res_col = int((image_col- filter_col+ 2*padding_shape[1])/S +1)
    # output shape formula source: 
    # https://stackoverflow.com/questions/53580088/calculate-the-output-size-in-convolution-layer
    res = np.zeros([res_row,res_col])
    for i in range(res_row):
        for j in range(res_col):
            res[i,j] = np.sum(image[i:i+filter_row,j:j+filter_col] * filt)
    return res


# caso 1
image1 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]])
filt1 = np.array([[1,1,1],[0,0,0],[2,10,3]])
answer1 = np.array([[9, 67,225,271],[ 34,50,169,349],[ 91,106,108,110]])
res1 = conv(image1,filt1)
print("Resultado 1:")
print(res1)
print("Deberia ser:")
print(answer1)

#caso 2
image2 = np.array([[10,4,50,30,20],[80,0,0,0,6],[0,0,1,16,17],[0,1,0,7,23],[1,0,6,0,4]])
filt2 = np.array([[1,0,1],[0,0,0],[1,0,3]])
answer2 = np.array([[63,82,122],[80,22,75],[20,16,36]])
res2 = conv(image2,filt2)
print("Resultado 2:")
print(res2)
print("Deberia ser:")
print(answer2)