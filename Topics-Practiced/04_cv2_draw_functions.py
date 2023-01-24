import numpy as np
import cv2 as cv
# Create a black image
img = np.full((512, 512,3), 0, np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv.line(img, (0, 0), (200, 511), (255, 0, 0), 1)
cv.rectangle(img, (100,100),(500,500),(0,255,0),1)
cv.circle(img,(300,300),100,(255,255,0),3)
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[10,5],[20,400],[20,5],[40,400]], np.int32)
# pts = pts.reshape((-1, 1, 2))
cv.polylines(img,[pts],False,(0,255,255))
cv.putText(img,'OpenCV',(10,100), cv.FONT_ITALIC, 4,(255,255,255),2,cv.LINE_AA)

cv.circle(img,(256,150),50,(0,0,255),25)
cv.circle(img,(170,260),50,(0,255,0),25)
cv.circle(img,(340,260),50,(255,0,0),25)

print(img[260][160])

cv.imshow("line", img)
cv.waitKey(0)
cv.destroyAllWindows()