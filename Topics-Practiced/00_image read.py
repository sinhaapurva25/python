import cv2
import numpy as np
from matplotlib import pyplot as plt

print(cv2.__version__)
path = r'Images\38.jpg';
img = cv2.imread(path,-1);
cv2.imshow('image',img);
cv2.waitKey(0);
cv2.destroyAllWindows();

# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic');
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
# plt.show()