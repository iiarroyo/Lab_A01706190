import numpy as np
import filters

def padding(image, desired_padding):
    '''
    recibe imagen (np.array),  y el padding deseado (tupla)
    devuelve imagen con padding
    '''
    image_row,image_col=image.shape
    pad_height = desired_padding[0]
    pad_width = desired_padding[1]

    #matriz con columnas y renglones agregados de padding
    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))

    #matriz con imagen original embebida con for loop
    for i in range(padded_image.shape[0]):
        if (i>=(pad_height) and i<(image_row+pad_height)):
            for j in range(padded_image.shape[1]):
                if((j>=(pad_width)) and j<(image_col+pad_width)):
                    padded_image[i,j] = image[i-pad_height,j-pad_width]

    return padded_image

# caso 1
result = padding(filters.gaussian_blur,[1,1])
print(result)