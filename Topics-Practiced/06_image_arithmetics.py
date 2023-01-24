import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path1=r'0.6286412288950787.jpg'
path2=r'0.6286412288950787.jpg'

img1=cv.imread(path1, cv.IMREAD_REDUCED_COLOR_8)
img2=cv.imread(path2, cv.IMREAD_REDUCED_COLOR_8)

add_cv=cv.add(img1,img2)
add_numpy=img1+img2
addweighted=cv.addWeighted(img1,0.1,img2,0.1,0)

b_add_cv,g_add_cv,r_add_cv=add_cv[:,:,0],add_cv[:,:,1],add_cv[:,:,2]
add_cv[:,:,2]=r_add_cv
add_cv[:,:,0]=b_add_cv

b_add_numpy,r_add_numpy=add_numpy[:,:,2],add_numpy[:,:,0]
add_numpy[:,:,2]=r_add_numpy
add_numpy[:,:,0]=b_add_numpy

b_addweighted,r_addweighted=addweighted[:,:,2],addweighted[:,:,0]
addweighted[:,:,2]=r_addweighted
addweighted[:,:,0]=b_addweighted

plt.subplot(131),plt.imshow(add_cv,'gray'), plt.title("ADD_CV")
plt.subplot(132),plt.imshow(add_numpy,'gray'), plt.title("ADD_NUMPY")
plt.subplot(133),plt.imshow(addweighted,'gray'), plt.title("ADDWEIGHTED")
plt.show()

# cv.imshow("add_cv", add_cv)
# cv.imshow("add_numpy", add_numpy)
# cv.imshow("addweighted", addweighted)
# cv.waitKey(0)
# cv.destroyAllWindows()