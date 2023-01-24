import cv2 as cv

path = r'Images/roi.jpg'
img = cv.imread(path)
cv.imshow("imggg",img)
ball = img[228:279, 270:320]
img[214:265, 80:130] = ball

# zero,one,two = cv.split(img)
# img = cv.merge((one,zero,two))
# #blue and green channels interchanged

# # setting the nth channel to 0
# img[:,:,2] = 0
# img[:,:,1] = 0
# img[:,:,0] = 0
# print(img[:,:,2])

zero,one,two= img[:,:,2], img[:,:,1], img[:,:,0]
img = cv.merge((one,zero,two))

cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()