import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread(r'Images/38.jpg', cv.IMREAD_REDUCED_GRAYSCALE_8)
img=cv.medianBlur(img,5)

ret1,thresh1=cv.threshold(img,127,255,cv.THRESH_BINARY)
ret2,thresh2=cv.threshold(img,127,255,cv.THRESH_BINARY)
ret3,thresh3=cv.threshold(img,127,255,cv.THRESH_MASK)
ret4,thresh4=cv.threshold(img,50,255,cv.THRESH_TRUNC)
ret5,thresh5=cv.threshold(img,50,255,cv.THRESH_TOZERO)
ret6,thresh6=cv.threshold(img,50,255,cv.THRESH_MASK)
ret7,thresh7=cv.threshold(img,50,255,cv.THRESH_BINARY_INV)
ret8,thresh8=cv.threshold(img,50,255,cv.THRESH_TOZERO_INV)

images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6, thresh7, thresh8]
title = [img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6, thresh7, thresh8]

for i in range(9):
    e1 = cv.getTickCount()
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray'),plt.title(title[i]), plt.xticks([]), plt.yticks([])
    e2 = cv.getTickCount()
    time=(e2-e1)/cv.getTickFrequency()
    print(i,": cv.getTickCount()= ",time,", cv.getTickFrequency()= ",cv.getTickFrequency())

# plt.subplot(3,3,1),plt.imshow(img,'gray'),plt.title("img"),plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,2),plt.imshow(thresh1,'gray'),plt.title("thresh1"),plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,3),plt.imshow(thresh2,'gray'),plt.title("thresh2"),plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,4),plt.imshow(thresh3,'gray'),plt.title("thresh3"),plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,5),plt.imshow(thresh4,'gray'),plt.title("thresh4"),plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,6),plt.imshow(thresh5,'gray'),plt.title("thresh5"),plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,7),plt.imshow(thresh6,'gray'),plt.title("thresh6"),plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,8),plt.imshow(thresh7,'gray'),plt.title("thresh7"),plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,9),plt.imshow(thresh8,'gray'),plt.title("thresh8"),plt.xticks([]), plt.yticks([])
plt.show()
print(cv.useOptimized())