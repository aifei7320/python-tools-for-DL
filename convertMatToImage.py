import matplotlib.pyplot as plt
import numpy as np, cv
import scipy.io as sio
from PIL import Image
import sys
import cv2

w = int(sys.argv[2])
h = int(sys.argv[3])
z = int(sys.argv[4])
origin_data = sio.loadmat(sys.argv[1])
data = origin_data['data']
array = np.zeros([w,h,z])
array = data

gray = np.zeros((513,513), np.float32)

print(gray.shape)
for i in range(w):
    for j in range(h):
        gray[i, j] = np.argmax(array[i, j, :]) 

img = gray.reshape(w, h).T
new_img = cv.fromarray(gray)
vis = cv.CreateMat(h, w, cv.CV_32FC3)
cv.CvtColor(new_img, vis, cv.CV_GRAY2BGR)
print(type(vis))
cv2.imwrite('vis.jpg', img)
#new_img.save('new.jpg')
#plt.imshow(img)
#plt.show()
