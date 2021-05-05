# Israel Arroyo A01706190
# conv.py
# segunda version, funcion que recibe tamaño de imagen variable
import numpy as np
import cv2
import matplotlib.pyplot as plt
import filters

def conv(image, filt, padding_shape=[1,1]):
    '''
    recibe imagen, filtro/kernel y el shape de padding deseado
    devuelve convolucion valida
    '''
    S = 1 # default: no stride
    # default: no padding
    filter_row,filter_col = filt.shape
    image_row,image_col=image.shape
    res_row = int((image_row - filter_row + 2*padding_shape[0])/S +1)
    res_col = int((image_col - filter_col+ 2*padding_shape[1])/S +1)
    # output shape formula source: 
    # https://stackoverflow.com/questions/53580088/calculate-the-output-size-in-convolution-layer
    res = np.zeros([res_row,res_col])

    pad_height = int((filter_row - 1) / 2)
    pad_width = int((filter_col - 1) / 2)

    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image

    for i in range(res_row):
        for j in range(res_col):
            res[i,j] = np.sum(padded_image[i:i+filter_row,j:j+filter_col] * filt)
    return res


image = cv2.imread("noki.jpg",cv2.IMREAD_GRAYSCALE)
filt = filters.gaussian_blur
# print(filt)
result = conv(image,filt)
cv2.imshow('imagen original',image)
cv2.waitKey(0)
plt.imshow(result,cmap='gray')
plt.title("imagen blur")
plt.show()