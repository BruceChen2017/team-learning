"""
    https://github.com/datawhalechina/team-learning
    https://stackoverflow.com/questions/19815732/what-is-gradient-orientation-and-gradient-magnitude
"""
import cv2
import numpy as np 
from matplotlib import pyplot as plt

src = cv2.imread("bw.png")
img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# sobel
sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)
sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)
plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(1,3,2),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(1,3,3),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

# Canny
src = cv2.imread("butterfly.tiff")
img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# canny边缘检测
img1 = cv2.GaussianBlur(img,(3,3),0)
canny = cv2.Canny(img1, 50, 200)

# 画图
plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(1,2,2),plt.imshow(canny,cmap = 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])
plt.show()