import numpy as np
import cv2
import matplotlib.pyplot as plt


image = cv2.imread("noki.jpg",cv2.IMREAD_GRAYSCALE)
h = [0]*256
for value in range(256):
    h[value] = (image==value).sum()
plt.bar(range(256),h)
plt.show()

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)